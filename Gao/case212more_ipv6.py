import os
info = " \"China\" \"Shaanxi\" \"baoji\" \"CTCC\" \"114.196428\" \"22.353541\""
n = -1
m = -1
all_dc = ""
dc = ""
for i in range(30):
    n += 1
    p = hex(n)[2:]
    m = -1
    for j in range(65535):
        m += 1
        q = hex(m)[2:]
        dc = "7777:7777:7777:7777:7777:7777:" + str(p) + ":" + str(q) + "/128" + info + "\n"
        all_dc += dc
f = open("Gao/China_IPv6" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()