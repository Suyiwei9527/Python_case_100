#  curl --http2-prior-knowledge http://172.17.1.45:80 -H "cookie: a=1"
import os
n = 0
all_dc = ""
prefix = ""
for i in range(2500):
    #prefix = "GET / HTTP/1.1" + "\n" + "Host: 172.17.1.148" + "\n"
    prefix = "wrk.method = \"GET\"" + "\n"
    n += 1
    #dc = "Connection" + ": " + "a" + str(n) + "\n"
    dc = "wrk.headers[\"Connection" + str(n) + "\"] = \"b" + str(n) + "\"\n"
    all_dc += dc
prefix = prefix + all_dc
f = open("Gao/wrk_header_1w.lua" , "w+",encoding="utf-8")
f.write(prefix)
f.close()