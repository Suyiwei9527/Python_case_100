#实现最大公约数算法
def gcd(x1,x2):
    if x1 > x2:
        x1,x2 = x2,x1
    for i in range(1,x1+1):
        if x1 % i == 0:
            if x2 % i == 0:
                gcd = i
    return gcd
n1 = int(input("Please input a number:\n"))
n2 = int(input("Please input an another number:\n"))
n3=gcd(n1,n2)
print("%d is %d and %d 's gcd"%(n3,n1,n2))