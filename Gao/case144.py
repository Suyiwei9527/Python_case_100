#spilt
import re
t = open("querry.txt","r")
f = t.readlines()
result = ''
for line in f:
    p = ((re.search('T_\w{1,10}',line).group()))
    p = p.split("T_")[1]
    result += p + "\n"
t.close()
new = open("result.txt","w")
new.write(result)
new.close()