#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
l=[12,21,23,41,45,76,86,94]
l.append(int(input("plase enter a number:")))
if l[-2]>l[0]:
	for i in range(len(l)):
		if l[i]>l[-1]:
			l[i],l[-1]=l[-1],l[i]
else:
	for i in range(len(l)):
		if l[i]<l[-1]:
			l[i],l[-1]=l[-1],l[i]
print(l)