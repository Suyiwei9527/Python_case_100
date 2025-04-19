#slb real http "Gao_1_1" 88.8.1.1 80 0 http 3 3
##slb real health Gap_add_hc_40_2 Gao_1_2 88.8.40.2 80 http 3 3
#slb group member Gao_rr Gao_10_10
#ssl host real Gao_r Gao_1_50000
import os
info = "slb real http "
info2 = "slb real health add_httphc_"
info3 = "slb group member Gao_rr "
info4 = "ssl host real Gao_r "
info4_2 = "ssl host real Gao_r_2 "
info4_3 = "ssl host real Gao_r_3 "
info4_4 = "ssl host real Gao_r_4 "
n = 0
#m = -1
all_dc = ""
dc = ""
for i in range(160):
    n += 1
    z = n + 160
    p = hex(n)[2:]
    m = 49999
    for j in range(50):
        m += 1
        rsname = "Gao_" + str(n) + "_" + str(m)
        dc3 = info2 + str(z) + "_" + str(m) + " " + rsname + " 88.8.2." + str(z) + " " + str(m)  + " http 3 3" + "\n"
        dc2 = info3 + rsname + "\n"
        dc1 = info + rsname + " 88.8.2." + str(n) + " " + str(m) + " 0 http 3 3" + "\n"
        if n < 41:
            dc4 = info4 + rsname + "\n"
            dc = dc1 + dc2 + dc3
            all_dc += dc
        elif n < 81:
            dc4 = info4_2 + rsname + "\n"
            dc = dc1 + dc2 + dc3
            all_dc += dc
        elif n < 121:
            dc4 = info4_3 + rsname + "\n"
            dc = dc1 + dc2 + dc3
            all_dc += dc
        else:
            dc4 = info4_4 + rsname + "\n"
            dc = dc1 + dc2 + dc3
            all_dc += dc
f = open("/root/rs_http_8000.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()