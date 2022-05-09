#re.search
import re
t = open("querry.txt","r",encoding="utf-8")
f = t.readlines()
result = ''
for line in f:
    p = (re.search('\d{1,5}\s{10,}',line).group())
    result += p + "\n"
t.close()
new = open("result_number.txt","w",encoding="utf-8")
new.write(result)
new.close()