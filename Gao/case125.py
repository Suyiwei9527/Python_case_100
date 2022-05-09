#定义一个整型数组，并计算元素之和
import random
s=0
l=[]
for i in range (10):
    l.append(random.randint(1,100))
print(l)
for i in range(len(l)):
    s += l[i]
print(s)