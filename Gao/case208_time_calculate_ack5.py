import re
import datetime

with open('c2_2.txt', 'r') as file:
    lines = file.readlines()

time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}.\d{6})')
seq_dict = {}

with open('diff_2.txt', 'w',encoding="utf-8") as output_file:
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
            #print(f"Seq: {ack_num}, Time difference: {time_diff}")