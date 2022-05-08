#读目录下所有文件的第一行，写入另一文件
import os
import re
pathdir = "G:\\TEST"
files = os.listdir(pathdir)
files.sort(key = lambda i:int(re.search('(\d+)',i).group()))
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