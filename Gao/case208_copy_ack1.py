with open('a2.txt', 'r', encoding='utf-16') as infile:
    with open('b2.txt', 'w+', encoding='utf-8') as outfile:
        for line in infile:
            if 'Flags [S]' in line:
                outfile.write(line)
            elif 'Flags [S.]' in line:
                outfile.write(line)