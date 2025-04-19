#for i in dc_21 dc_22
import os
n = 20
all_dir = ""
for i in range(25):
    n += 1
    dir = "dc_" + str(n) + " "
    all_dir += dir
f = open("Gao/dirs.txt" , "w+",encoding="utf-8")
f.write(all_dir)
f.close()