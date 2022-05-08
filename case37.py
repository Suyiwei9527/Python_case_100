#对10个数进行排序
print("please input 10 number")
l=[]
for i in range(10):
	l.append(int(input("please enter a number:")))
for i in range(9):
	for j in range(i+1,10):
		if l[i] > l[j]:
			l[i],l[j]=l[j],l[i]
print(l)