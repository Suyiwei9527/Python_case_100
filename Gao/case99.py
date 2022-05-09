#文件A和B,各存放一行字母,两个文件信息按字母顺序排列输出到文件C中
n = open("A.txt","w")
m = open("B.txt","w")
n.write("edc")
m.write("qaz")
n = open("A.txt","r")
m = open("B.txt","r")
a = n.read()
b = m.read()

l = list(a + b)
l.sort()
s = ""
s = s.join(l)
f = open("C.txt","w")
f.write(s)
f = open("C.txt","r")
print(f.read())
n.close
m.close
f.close