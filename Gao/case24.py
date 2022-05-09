#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
from functools import reduce
l=[]
a=2
b=1
l.append(a/b)
for n in range (1,20):
    b,a=a,a+b
    l.append(a/b)
print("%.5f" %(reduce(lambda x,y:x+y,l)))