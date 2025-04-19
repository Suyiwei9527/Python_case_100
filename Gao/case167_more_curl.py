#  curl --http2-prior-knowledge http://172.17.1.45:80 -H "cookie: a=1"
import os
n = 9999
all_dc = ""
prefix = ""
for i in range(600):
    prefix = "curl --http2-prior-knowledge http://172.17.1.45:80 "
    n += 1
    dc = "-H \"cookie: " + str(n) + "=" + str(n+10) + "\" "
    all_dc += dc
prefix = prefix + all_dc
f = open("Gao/curl_cookie.txt" , "w+",encoding="utf-8")
f.write(prefix)
f.close()