#slb real http "Gao_1_1" 88.8.1.1 80 0 http 3 3
##slb real health Gap_add_hc_40_2 Gao_1_2 88.8.40.2 80 http 3 3
#slb group member Gao_rr Gao_10_10
#ssl host real Gao_r Gao_1_50000
import os
info = "sdns service ip service_"
info2 = "sdns monitor http monitor_"
info3 = " \"HEAD / HTTP/1.0\\r\\n\\r\\n\" \"200\" \"up\" 10 10 2 88.8."
info4 = " 8080 0.0.0.0 0.0.0.0"
info5 = "sdns host name \"gaov"
info6 = ".test\" 10"
info7 = "sdns pool name gaov"
info8 = "sdns pool method primary gaov"
info9 = "sdns policy default \"gaov"
info10 = ".test\" gaov"
info11 = "sdns health match mode monitor_"
incfo12 = "sdns service monitor apply service_"
info13 = "sdns health import request request_"
info14 = " \"http://172.16.75.15/request/request"
info15 = "sdns health import response respense_"
info16 = " \"http://172.16.75.15/response/respense"
info17 = "sdns health bind monitor_"
info18 = " \"HEAD / HTTPS/1.0\\r\\n\\r\\n\" \"200\" \"up\" 10 10 2 88.8."
info19 = "sdns monitor https monitor_"
n = 0
all_dc = ""
dc = ""
for i in range(4):
    n += 1
    z = n + 160
    p = hex(n)[2:]
    m = 0
    for j in range(255):
        m += 1
        q = (n-1)*255 + m
        dc1 = info + str(q) + " " + " 88.8." + str(n) + "." + str(m) + " 0" + "\n"
        dc2 = info2 + str(q) + info3 + str(n) + "." + str(m) + info4 + "\n"
        dc3 = info5 + str(q) + info6 + "\n"
        dc4 = info7 + str(q) + " 3" + "\n"
        dc5 = info8 + str(q) + " ipo" + "\n"
        dc6 = info9 + str(q) + info10 + str(q) + "\n"
        dc7 = info11 + str(q) + " 0" + "\n"
        dc8 = incfo12 + str(q) + " monitor_" + str(q) + "\n"
        dc9 = info13 + str(q) + info14 + "\"" +"\n"
        dc10 = info15 + str(q) + info16 + "\"" +"\n"
        dc11 = info17 + str(q) + " request_" + str(q) + " respense_" + str(q) +"\n"
        dc2_2 = info19 + str(q) + info18 + str(n) + "." + str(m) + info4 + "\n"
        if q < 501:
            dc = dc1 + dc2 + dc3 + dc4 + dc5 + dc6 + dc7 + dc8 + dc9 + dc10 + dc11
            all_dc += dc
        elif q < 901:
            dc = dc1 + dc2 + dc7 + dc8 + dc9 + dc10 + dc11
            all_dc += dc
        elif q <1001:
            dc = dc1 + dc2_2 + dc7 + dc8 + dc9 + dc10 + dc11
        #dc = dc1
            all_dc += dc
f = open("Gao/sdns.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()