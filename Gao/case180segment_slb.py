#slb virtual ftp "gao_1_vs_3@@gao_1" 1237::1:0:3 800 0
#slb virtual http "gao_1_vs_2@@gao_1" 1237::1:0:2 800 arp 0
#slb virtual diameter "gao_1_vs_4@@gao_1" 1237::1:0:4 800 arp 0
#dc = "ip pool \"gao_" + str(n)+ "_pool_1@@gao_" + str(n)+ "\" 1237::" + str(m) + ":0:9 1237::" + str(m) + ":0:9" + "\n"
#dc = "slb real http \"gao_" + str(n)+ "_rs_" + str(m)+ "@@gao_" + str(n)+ "\" 1237::200:0:" + str(q) + " 800 0 none 3 3" + "\n"
import os
n = -1
all_dc = ""
dc = ""
for i in range(512):
    n += 1
    p = hex(n)[2:]
    m = 1
    for j in range(15):
        m += 1
#        all_dc += dc
        if j == 0:
            dc = "slb virtual ftp \"gao_" + str(n)+ "_vs_" + str(m)+ "@@gao_" + str(n)+ "\" 1237::" + str(p) + ":0:" + str(m) + " 800 0" + "\n"
            all_dc += dc
        elif j == 1:
            dc = "slb virtual diameter \"gao_" + str(n)+ "_vs_" + str(m)+ "@@gao_" + str(n)+ "\" 1237::" + str(p) + ":0:" + str(m) + " 800 arp 0" + "\n"
            all_dc += dc
        elif j < 7:
            dc = "slb virtual http \"gao_" + str(n)+ "_vs_" + str(m)+ "@@gao_" + str(n)+ "\" 1237::" + str(p) + ":0:" + str(m) + " 800 arp 0" + "\n"
            all_dc += dc
        else:
            dc = "slb virtual http \"gao_" + str(n)+ "_vs_" + str(m)+ "@@gao_" + str(n)+ "\" 1237::" + str(p) + ":0:8 " + str(m) + " arp 0" + "\n"
            all_dc += dc
f = open("Gao/segment_slb.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()