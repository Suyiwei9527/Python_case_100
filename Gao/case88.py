#读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*
for i in range(7):
	l=[]
	a = int(input("Please enter a number:"))
	if a <1 or a > 50:
		print("Your numbers do not meet the rules")
	else:
		for j in range(a):
			l.append("*")		
		print("".join(str(k) for k in l))