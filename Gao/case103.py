#以下实例为通过用户输入数字，并计算二次方程
import cmath
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = (b**2) -(4*a*c)
x1 = (-b + cmath.sqrt(d)) / (2*a)
x2 = (-b - cmath.sqrt(d)) / (2*a)
print("the result is {0} {1}" .format(x1,x2))