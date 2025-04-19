with open('b2.txt', 'r', encoding='utf-8') as file:
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
    elif 'Flags [S.]' in line:
        output_lines.append(line)

with open('b2_2.txt', 'w+') as file:
    file.writelines(output_lines)