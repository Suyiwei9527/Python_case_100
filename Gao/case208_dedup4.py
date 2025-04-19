with open('c2.txt', 'r', encoding='utf-8') as infile:
    with open('c2_2.txt', 'w+', encoding='utf-8') as outfile:
        ack_values = set()
        for line in infile:
            if 'Flags [S]' in line:
                outfile.write(line)
            elif 'Flags [S.]' in line:
                ack_value = line.split("ack ")[1].split(",")[0]
                if ack_value not in ack_values:
                    ack_values.add(ack_value)
                    outfile.write(line)
