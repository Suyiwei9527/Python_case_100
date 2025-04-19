import re
with open('b2_2.txt', 'r', encoding='utf-8') as file1, open('c2.txt', 'w+', encoding='utf-8') as file2:
    for line in file1:
        match = re.search(r'(\d+:\d+:\d+\.\d+)', line)
        if match:
            seq_match = re.search(r'seq (\d+)', line)
            ack_match = re.search(r'ack (\d+)', line)
            if ack_match:
                ack_value = int(ack_match.group(1)) - 1
                line = re.sub(r'ack (\d+)', f'ack {ack_value}', line)
            file2.write(line)