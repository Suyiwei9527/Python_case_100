#读目录下所有文件的第一行，写入另一文件
import os
import re
pathdir = "D:\\Python_case_100\\Gao"
files = os.listdir(pathdir)
#files.sort(key = lambda i:int(re.search('(\d+)',i).group()))
files.sort(key=lambda x: int(re.search(r'(\d+)', x).group(1)) if re.search(r'\d+', x) else 0)
title = ""
line = ""
name = ""
n = 0
for file in files:
    all_f = open("%s" %file,"r",encoding="utf-8")
    name = file.split(".")[0]
    line = all_f.readline()
    n += 1
    title += name + ":" + line + "\n"
all_f.close()
f = open("100case_title.txt" , "w+",encoding="utf-8")
f.write(title)
f.close()