#www.gaov6_2.com AAAA
import os
all_dc = ""
n = 0
for i in range(500):
    n += 1
    dc = "gaov" + str(n) + ".test A" + "\n"
    all_dc += dc
f = open("Gao/dnsperf.txt" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()