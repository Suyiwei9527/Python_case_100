#求输入数字的平方，如果平方运算后小于 50 则退出。
from sys import flags
flag=1
while flag==1:
    a=int(input("请输入一个数字（若输入数字的平方和小于50程序则会退出）："))
    if a*a<50:
        flag=0
    elif a*a>50 or a*a==50:
        print("a的平方为%d"%(a*a))
        flag=1