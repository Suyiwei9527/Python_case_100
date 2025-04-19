'''
sudo ip link add link ens224 name ens224.8 type vlan id 8
ip addr add 22.205.8.253/24 dev ens224.8
ip link set dev ens224.8 up
'''
import os
n = 0
all_dc = ""
info = "vlan port4 Gao_"
info_1 = "no vlan Gao_"
info2 = "ip address Gao_"
info3 = " 255.255.255.0"
info4 = "ip link add link ens224 name ens224."
info5 = " type vlan id "
info6 = "ip addr add 77."
info7 = "/24 dev ens224."
info8 = "ip link set dev ens224."
info9 = "slb real http Gao_"
info10 = " 80 0 icmp 10 1"
info11 = "mnet bond1 mnet_"
info12 = "ha group fiprange 10 2021:1::"
for i in range(16):
    n += 1
    m = 0
    for j in range(255):
        m += 1
        q = (n-1)*255 + m
        if q <= 50:
        #dc1 = info4 + str(q+2000) + info5 + str(q+2000) + "\n"
        #dc2 = info6 + str(n) + "." + str(m) + ".5" + info7 + str(q+2000) + "\n"
        #dc3 = info8 + str(q+2000) + " up\n"
        #dc4 = info + str(q) + " " + str(q) + "\n"
        #dc5 = info_1 + str(q+2000) + "\n"
        #dc6 = info2 + str(q) + " 77." + str(n) + "." + str(m) + ".7" + info3 + "\n"
        #dc7 = "no " + info2 + str(q+2000) + "\n"
        #dc8 =  "77." + str(n) + "." + str(m) + ".1" + "\n"
        #dc9 =  "77." + str(n) + "." + str(m) + ".3" + "\n"
        #dc10 = info9 + str(q) + " 77." + str(n) + "." + str(m) + ".5" + info10 + "\n"
            dc11 = info12 + str(q) + ":1 2021:1::" + str(q) + ":100 mnet_1" + "\n"
            dc =  dc11
            all_dc += dc
f = open("Gao/vlan_fiprange.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()