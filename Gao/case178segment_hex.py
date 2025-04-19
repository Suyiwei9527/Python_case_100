#segment ip address vlan_1000 2023:0::1 96 "auto"
import os
n = 4
all_dc = ""
for i in range(50):
    n += 1
    m = hex(n)[2:]
    dc = "segment ip address vlan_" + str(n+1000) + " 2023:" + str(m) + "::1 96 \"auto\"" + "\n"
    all_dc += dc
f = open("Gao/segment_ipadd.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()