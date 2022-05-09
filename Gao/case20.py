#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height= []
tour= []
high=100
n=10
for i in range (1, n+1):
	if i ==1:
		tour.append(high)
	else:
		tour.append(high*2)
	high /= 2
	height.append(high)
print("The total : tour = {0}" .format(sum(tour)))
print("Back High: height = {0}" .format(height[-1]))