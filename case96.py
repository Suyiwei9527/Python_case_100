#计算字符串中子串出现的次数
a="Hello Yang Guo Yang Guo"
b="Yang"
l=a.split()
k=[]
k.append(b)
count=0
for i in range(len(l)):
	if k[0] == l[i]:
		count += 1
print(count)