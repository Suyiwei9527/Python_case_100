def write_to_file(content):
    with open("d2.txt" , "w+",encoding="utf-8") as file:
        file.write(content)
def write_to_file2(content):
    with open("d2_srcport.txt" , "w+",encoding="utf-8") as file:
        file.write(content)

all_time = ""
all_tshark = ""
with open('diff_2.txt', 'r', encoding='utf-8') as file:
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
            timeevery = a0 +" " + a +" " + c0 +" " + c1 + f"\'s time(" + b + f") diff is too large" + "\n"
            all_time += timeevery
            write_to_file(all_time)
            write_to_file2(write_tshark)
            print(line.split()[1], '\'s time diff is too large')
            data_found = True
    if not data_found:
        print('no time diff is too large')