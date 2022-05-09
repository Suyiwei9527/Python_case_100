#输入三个整数x,y,z，请把这三个数由小到大输出。
a=int (input("请输入一个整数："))
b=int (input("请输入一个整数："))
c=int (input("请输入一个整数："))
list=[a,b,c]
list.sort()
print(list)