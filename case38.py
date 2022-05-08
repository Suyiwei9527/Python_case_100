#求一个3*3矩阵主对角线元素之和
l=[]
for i in range (3):
	l.append([])
	for j in range(3):
		l[i].append(int(input("please input a number:")))
sum=0
for i in range (3):
	sum +=l[i][i]
print(sum)