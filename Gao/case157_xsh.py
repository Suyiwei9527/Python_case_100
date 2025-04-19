'''
slb real health "add_hc_v6_" + str(n) + "_http" "gao_rs" + str(n) + "_http_v6" 2021::204:1 800 http 3 3
slb real http "gao_rs" + str(n) + "_http_v6" 2021::204:" + str(n) + " 800 60000 none 3 3
slb group method Gao_v6_g_AXML_SVR_10011
slb group member Gao_v6_g_AXML_SVR_1
+ "	xsh.Screen.Send(\"slb group method Gao_v6_g_AXML_SVR_" + str(n) + "\" + \"\\n\")" + "\n" + every
+ "	xsh.Screen.Send(\"slb group member Gao_v6_g_AXML_SVR_" + str(n) + " gao_rs_158_\" + str(n) + \"\\n\")" + "\n" + every
health server add_hc_v6_" + str(n) + "_http 1 1
	  xsh.Screen.Send("con ter force" + "\n")
	  xsh.Screen.WaitForString("dc_39(config)#")
	  xsh.Session.Sleep(5000)
+ "	xsh.Session.Sleep(1000)" + "\n"
+ "	xsh.Screen.Send(\"con ter force\" + \"\\n\")" + "\n"
+ "	xsh.Screen.WaitForString(\"Gao(config)#\")" + "\n"
Sub Main
	xsh.Screen.Synchronous = true

dc3 = "ping " + " 77." + str(n) + "." + str(m) + ".3"
ha group fiprange 10 2021:1::4:1 2021:1::4:100 mnet_1
'''
import os
n = 0
end = "	xsh.Screen.Send(\"wr mem\" + \"\\n\")" + "\n" + "End Sub"
all_dc = "Sub Main" + "\n" + "	xsh.Screen.Synchronous = true" + "\n"
conf = "	xsh.Screen.Send(\"con ter force\" + \"\\n\")" + "\n"
every = "	xsh.Session.Sleep(5000)" + "\n" + "	xsh.Screen.WaitForString(\"CC-WL-WY-LTM03(config)#\")" + "\n"
info = "ha group fiprange 10 2021:1::"
for i in range(17):
    n += 1
    m = 0
    for j in range(255):
        m += 1
        q = (n-1)*255 + m
        p = hex(q)[2:]
        if q <= 31:
        #dc ="	xsh.Screen.Send(\"no slb virtual http Gao_seg_" + str(n) + "_v6 2021::1158:" + str(n) + " 800 60000 tcp 3 3\" + \"\\n\")" + "\n" + every + "	xsh.Screen.Send(\"slb group method Gaoxxxx_v6_g_AXML_SVR_" + str(n) + "\" + \"\\n\")" + "\n" + every + "	xsh.Screen.Send(\"slb group member Gaoxxxx_v6_g_AXML_SVR_" + str(n) + " gao_rs_1158_" + str(n) + "_tcp\" + \"\\n\")" + "\n" + every
        #dc = "	xsh.Screen.Send(\"ping 77." + str(n) + "." + str(m) + ".4" + " \" + \"\\n\")" + "\n" + every
            #dc = "	xsh.Screen.Send(\"ip address mnet_" + str(q) + " 2021:" + str(p) + "::1 64" + " \" + \"\\n\")" + "\n" + every
            dc = "	xsh.Screen.Send(\"" + info + str(q) + ":1 2021:1::" + str(q) + ":100 mnet_1" + " \" + \"\\n\")" + "\n" + every
        #dc ="	xsh.Screen.Send(\"no slb virtual http Gao_seg_" + str(n) + "_v6" + " \" + \"\\n\")" + "\n" + every
            all_dc += dc
        elif q == 32:
            dc = "	xsh.Screen.Send(\"" + info + str(q) + ":1 2021:1::" + str(q) + ":40 mnet_1" + " \" + \"\\n\")" + "\n" + every
            all_dc += dc
        #if i == 4000-1 :
all_dc += "End Sub"
f = open("Gao/mnet_fiprange.vbs" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()