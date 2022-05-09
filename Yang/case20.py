#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
all_hight=100
hight=100
for i in range(0,9):
    all_hight=all_hight+hight/pow(2,i)
print('第10次落地共经过%f米'%all_hight)
print('第10次的跳跃高度为%f'%float(100/pow(2,10)))
