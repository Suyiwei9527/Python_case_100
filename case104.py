#定义函数计算圆的面积
from re import S
def circle_s(r):
    pi = 3.1415926
    s = pi * r**2
    return(s)
r = int(input("Please input the circle's r:\n"))
s = circle_s(r)
print("r = %d,s = %0.3f" %(r,s))