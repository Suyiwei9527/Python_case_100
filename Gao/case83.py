#求0—7所能组成的奇数个数
sum=0
a=0
for i in range(1,9):
	#print(a)
	if i ==1:
		a=4
	elif i ==2:
		a=7*a
	else:
		a=8*a
	sum =sum + a
	print(sum)