import os

input_dir = 'Geoip'
output_file = 'China_IPv4'

with open(output_file, 'w+', encoding='utf-8') as outfile:
    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as infile:
            for line in infile:
                outfile.write(line)