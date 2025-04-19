'''ltm profile ssl /Common/http1 {
    app-service none
    defaults-from /Common/http
    proxy-type reverse
}'''
import os
n = 0
all_dc = ""
for i in range(41000):
    n += 1
    dc ="ltm profile ssl /Common/XEwX4NdVxKXqwp7Vxs6Z38Gs3m4urYCg4MNPBvJwYqG1t01m7TMMGuE8lajAsrGZEbx0xTig170rLlB5mDtpfzavs4h0KbopejPcJPiGj8E2AgvM3zgboebqxcz7c8Re" + str(n) + " {" + "\n" + "    app-service none" + "\n" + "    defaults-from /Common/http" + "\n" + "    proxy-type reverse" + "\n" + "}" + "\n"
    all_dc += dc
f = open("Gao/f5.conf" , "w+",encoding="utf-8")
f.write(all_dc)
f.close()