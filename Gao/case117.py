#实现最小公倍数算法
def lcm(x1,x2):
    if x1 < x2:
        x1,x2=x2,x1
    for i in range(1,x1+1):
        for j in range(1,x1+1):
            if (x1 * i == x2 * j):
                t =x1*i
                return t
n1 = int(input("Please input a number:\n"))
n2 = int(input("Please input an another number:\n"))
print("%d is %d and %d 's lcm"%(lcm(n1,n2),n1,n2))