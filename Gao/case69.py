#n个人围成一圈,从第一个人开始报数，凡报到3的人退出圈子，问最后留下的是原来第几号的那位
n = int(input("Please enter the total person:"))
l = []
for i in range(n):
	l.append(i+1)
k = 0
i = 0
m = 0
while m < n-1:
	if l[i] !=0 : k+=1
	if k ==3 : 
		l[i]=0
		k = 0
		m +=1
	i += 1
	if i == n : i = 0
for i in range(n):
	if l[i] != 0:
	    print("the answer is:%s" %l[i])