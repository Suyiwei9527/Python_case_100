import os
info = "    \"China\"   \"Shaanxi\" \"xian\"    \"CMCC\"    \"119.291347\"  \"26.077181\""
n = -1
#m = -1
all_dc = ""
dc = ""
for i in range(3):
    n += 1
    p = hex(n)[2:]
    m = -1
    for j in range(2):
        m += 1
        q = hex(m)[2:]
        v = -1
        for k in range(2):
            v += 1
            dc = "77." + str(n) + "." + str(m) + "." + str(v) + "/32" + info + "\n"
            all_dc += dc
f = open("Gao/China_IPv4" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()