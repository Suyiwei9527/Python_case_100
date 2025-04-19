import os
n = 0
all_dc = ""
for i in range(500):
    n += 1
    info = "sdns pool service gaov"
    info2 = " service_"
    #dc = "http xforwardedfor off " + "\"Gao_seg_" + str(n) + "_v6@@rzHiGTIuZUwrlWjY8Aq8ogVTxOyD8dSwqsjNbvkn6EH0RiU7eRvAyoiArQEm5TCvJsO3mPUsVqgnVUnhw8UiyXo3VAeAzivDehicBtqyfuGMQdSnEGNTgZHG5Qhk5FGe\"" + "\n"
    #dc = "slb virtual http \"Gao_seg_" + str(n) + "_v6@@rzHiGTIuZUwrlWjY8Aq8ogVTxOyD8dSwqsjNbvkn6EH0RiU7eRvAyoiArQEm5TCvJsO3mPUsVqgnVUnhw8UiyXo3VAeAzivDehicBtqyfuGMQdSnEGNTgZHG5Qhk5FGe\" 2024:2024:8ff:1005::2 " + str(n) + " arp 0" + "\n" + "http rewrite body on " + "\"Gao_seg_" + str(n) + "_v6@@rzHiGTIuZUwrlWjY8Aq8ogVTxOyD8dSwqsjNbvkn6EH0RiU7eRvAyoiArQEm5TCvJsO3mPUsVqgnVUnhw8UiyXo3VAeAzivDehicBtqyfuGMQdSnEGNTgZHG5Qhk5FGe\"" + "\n"
    #dc = "sdns service ip \"dc_100_" + str(ip) + "_800\" " +  "2021::100:" + str(ip) + " 800 " + "\"xa18_dc\" 1" + "\n"
    #dc = "slb group method Gao_tcp_g_" + str(n) + "\n" + "slb real tcp gao_rs_tcp_183_" + str(n) + " 2022::183:" + str(n) + " 80 0 tcp 1 10" + "\n" + "slb group member Gao_tcp_g_" + str(n) + " gao_rs_tcp_183_" + str(n) + "\n" + "slb group member Gao_tcp_g_" + str(n) + " gao_rs_tcp_150" + "\n" + "slb virtual tcp \"gao_vs_tcp_183_" + str(n) + "\" 2021::183:" + str(n) + " 80 arp 0" + "\n" + "slb policy default \"gao_vs_tcp_183_" + str(n) + "\" Gao_tcp_g_"  + str(n) + "\n"
    #dc = "slb real tcp gao_rs_tcp_183_" + str(n) + " 2022::183:" + str(n) + " 80 0 tcp 1 10" + "\n" + "slb group member more" + " gao_rs_tcp_183_" + str(n) + "\n" 
    #dc = "slb virtual tcp \"gao_183_" + str(n) + "_v6\" 2024:2024:8ff:1005::2" + str(n) + " arp 0" + "\n" + "slb policy default \"gao_183_" + str(n) + "_v6\" more" + "\n"
    #dc = "slb group method Gao_http_g_" + str(n) + "\n" + "slb real http gao_rs_http_184_" + str(n) + " 2022::184:" + str(n) + " 80 0 http 1 10" + "\n" + "slb group member Gao_http_g_" + str(n) + " gao_rs_http_184_" + str(n) + "\n" + "slb group member Gao_http_g_" + str(n) + " gao_rs_http_300_100" + "\n" + "slb virtual http \"gao_vs_http_184_" + str(n) + "\" 2021::184:" + str(n) + " 80 arp 0" + "\n" + "slb policy default \"gao_vs_http_184_" + str(n) + "\" Gao_http_g_"  + str(n) + "\n"
    #dc = "no sdns service monitor apply \"dc_101_"+ str(n) + "_800\" \"gao_hc_55\"" + "\n"
    #dc = "sdns service ip \"dc_101_" + str(n) + "_800\" 2021::101:" + str(n) + " 800 \"xa6309_dc\"" + "\n" + "sdns service monitor apply \"dc_101_"+ str(n) + "_800\" \"gao_hc_3_v6\"" + "\n"
    #dc = "synconfig peer \"ibnw84muikr5jo9rnkcpdfmw0u66na81ka2opc51rhe0cp77dmGao_130_" + str(n) +"\" " + "192.168.130." + str(n) + "\n"
    #dc = "sdns service monitor apply \"dc_101_" + str(n) + "_800\" \"gao_hc_55\"" + "\n"
    #dc = "health disable port " + str(n) + "\n"
    dc1 = info + str(n) + info2 + str(2*n-1) + "\n"
    dc2 = info + str(n) + info2 + str(2*n) + "\n"
    dc = dc1 + dc2
    all_dc += dc
f = open("Gao/pool_ser.cfg" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()