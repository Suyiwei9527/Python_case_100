#author:gaozc
import re
import datetime
from datetime import datetime
from collections import defaultdict

def write(content,file):
    with open(file , "w+",encoding="utf-8") as file:
        file.write(content)

def write_lines(content,file):
    with open(file , "w+",encoding="utf-8") as file:
        file.writelines(content)

def dedup(readfile,writefile):#Remove the duplicate syn packets
    with open(readfile, 'r', encoding='utf-16') as file:
        lines = file.readlines()
    output_lines = []
    seq_set = set()
    for line in lines:
        if 'Flags [S]' in line:
            seq_start = line.find('seq') + 4
            seq_end = line.find(',', seq_start)
            seq = int(line[seq_start:seq_end])
            if seq not in seq_set:
                output_lines.append(line)
                seq_set.add(seq)
    with open(writefile, 'w+') as file:
        file.writelines(output_lines)

dedup("tracevs.log","detracevs.log")
dedup("tracers.log","detracers.log")

with open('detracevs.log', 'r', encoding='utf-8') as infile1,\
     open('detracers.log', 'r', encoding='utf-8') as infile2,\
     open('all.log', 'w+', encoding='utf-8') as outfile:#merge the syn packet 
        for line in infile1:
            outfile.write(line)
        for line in infile2:
            outfile.write(line)

time_format = "%H:%M:%S.%f"
seq_dict = {}
with open('all.log', 'r') as file:
    for line in file:
        match = re.search(r"(?P<time>\d{2}:\d{2}:\d{2}\.\d+).*seq (?P<seq>\d+)", line)
        if match:
            time_str = match.group('time')
            seq_value = match.group('seq')
            time = datetime.strptime(time_str, time_format)
            if seq_value not in seq_dict:
                seq_dict[seq_value] = []
            seq_dict[seq_value].append(time)
all_diff = []
for seq, times in seq_dict.items():
    if len(times) > 1:
        time_diff = abs(times[0] - times[1])
        result = f"Seq {seq} \'s time difference is: {time_diff}\n"
        all_diff.append(result)
write_lines(all_diff,'diff.log')

all_timeevery = []
with open('diff.log', 'r', encoding='utf-8') as file:
    data_found = False
    for line in file:
        if line.split()[-1] > '0:00:01.000000':
            seqvalue = line.split()[1]
            aseq = line.split()[0]
            #c0 = line.split()[2]
            #c1 = line.split()[3]
            timevalue = line.split()[-1]
            #tshark = "(tcp.port == " +c1 +") || "
            #all_tshark += tshark
            #write_tshark = "tshark -r a2.pcap -Y \"" + all_tshark + "\" -w delay.pcap"
            timeevery = aseq +" " + seqvalue + " " + f"\'s time(" + timevalue + f") diff is too large" + "\n"
            all_timeevery.append(timeevery)
            print(timeevery)
            data_found = True
    write_lines(all_timeevery,'result.log')
    if not data_found:
        print('no time diff is too large')