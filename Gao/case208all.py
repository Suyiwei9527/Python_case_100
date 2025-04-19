#author:gaozc
import re
import datetime

def write_lines(content,file):
    with open(file , "w+",encoding="utf-8") as file:
        file.writelines(content)

def write(content,file):
    with open(file , "w+",encoding="utf-8") as file:
        file.write(content)

with open('trace.log', 'r', encoding='utf-16') as infile:#抓包原始文件
    with open('syn-ack.log', 'w+', encoding='utf-8') as outfile:#取出[S]、[S.]包
        for line in infile:
            if 'Flags [S]' in line:
                outfile.write(line)
            elif 'Flags [S.]' in line:
                outfile.write(line)

with open('syn-ack.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()
output_lines = []
seq_set = set()
for line in lines:
    if 'Flags [S]' in line:
        seq_start = line.find('seq') + 4
        seq_end = line.find(',', seq_start)
        seq = int(line[seq_start:seq_end])
        if seq not in seq_set:#去掉重复的[S]包
            output_lines.append(line)
            seq_set.add(seq)
    elif 'Flags [S.]' in line:
        output_lines.append(line)
write_lines(output_lines,'dedup.log')

with open('dedup.log', 'r', encoding='utf-8') as file1, open('dedup2.log', 'w+', encoding='utf-8') as file2:
    for line in file1:
        match = re.search(r'(\d+:\d+:\d+\.\d+)', line)
        if match:
            seq_match = re.search(r'seq (\d+)', line)
            ack_match = re.search(r'ack (\d+)', line)
            if ack_match:
                ack_value = int(ack_match.group(1)) - 1#ack-1便于比对时间
                line = re.sub(r'ack (\d+)', f'ack {ack_value}', line)
            file2.write(line)

with open('dedup2.log', 'r', encoding='utf-8') as infile:
    with open('dedup3.log', 'w+', encoding='utf-8') as outfile:
        ack_values = set()
        for line in infile:
            if 'Flags [S]' in line:
                outfile.write(line)
            elif 'Flags [S.]' in line:
                ack_value = line.split("ack ")[1].split(",")[0]
                if ack_value not in ack_values:#去掉重复的[S.]包
                    ack_values.add(ack_value)
                    outfile.write(line)

with open('dedup3.log', 'r') as file:
    lines = file.readlines()
time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}.\d{6})')
seq_dict = {}
with open('diff.log', 'w+',encoding="utf-8") as output_file:#比对时间差异
    for line in lines:
        if 'Flags [S]' in line:
            seq_time = time_pattern.search(line).group(1)
            seq_num = int(re.search(r'seq (\d+),', line).group(1))
            seq_dict[seq_num] = seq_time
        elif 'Flags [S.]' in line:
            ack_time = time_pattern.search(line).group(1)
            ack_num = int(re.search(r'ack (\d+),', line).group(1))
            result = re.search(r'> \d+.\d+.\d+.\d+.(\d+)', line).group(1)
            if ack_num in seq_dict:
                time_diff = datetime.datetime.strptime(ack_time, '%H:%M:%S.%f') - datetime.datetime.strptime(seq_dict[ack_num], '%H:%M:%S.%f')
                output_file.write(f"Seq {ack_num} srcport {result} \'s time difference is: {time_diff}\n")

all_time = []
all_tshark = ""
with open('diff.log', 'r', encoding='utf-8') as file:
    data_found = False
    for line in file:
        if line.split()[-1] > '0:00:01.000000':
            a = line.split()[1]
            a0 = line.split()[0]
            c0 = line.split()[2]
            c1 = line.split()[3]
            b = line.split()[-1]
            tshark = "(tcp.port == " +c1 +") || "
            all_tshark += tshark
            write_tshark = "tshark -r a2.pcap -Y \"" + all_tshark + "\" -w delay.pcap"
            timeevery = a0 +" " + a +" " + c0 +" " + c1 + f"\'s time diff(" + b + f") is too large" + "\n"
            all_time.append(timeevery)
            print(timeevery)
            data_found = True
    write(write_tshark,"srcport.log")
    write_lines(all_time,"delay.log")
    if not data_found:
        print('no time diff is too large')