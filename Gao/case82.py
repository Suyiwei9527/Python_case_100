#八进制转换为十进制
l=[]
s=0
n=input("input a octal number:\n")
for i in range (len(n)):
	l.append(n[i])
for i in range (-1,-len(n)-1,-1):
	#print((l[i])*(8**(-i-1)))
	s = s + int(l[i])*(8**(-i-1))
print(s)