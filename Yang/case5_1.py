#斐波那契数列。
n=int(input('您想要计算到斐波那契数列的第几个值：请输入一个整数：'))
list_fei=[]
list_fei.append(0)
list_fei.append(1)
for i in range(2,n):
    list_fei.append(list_fei[i-1]+list_fei[i-2])
print (list_fei)