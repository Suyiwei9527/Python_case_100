with open('D:/Python_case_100/YunShangfuzai', 'r', encoding='utf-8') as infile:
    with open('D:/Python_case_100/Gao/PLM80598.cfg', 'w+', encoding='utf-8') as outfile:
        for i in range(4161):
            line = infile.readline()
            outfile.write(line)