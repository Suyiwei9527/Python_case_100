#author:gaozc
import re
import datetime
source_ip = '88.8.1.1'
all_port = ''
with open('src.txt', 'r', encoding='utf-16') as infile:
    for line in infile:
        match = re.search(r'(' + re.escape(source_ip) + r'\.(\d+)) > ', line)
        if match:
            srcport = int(match.group(2))
            if 56700 < srcport < 56749:
                print(f"port: {srcport} cannot use")