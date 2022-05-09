#输入一个数判断是否为质数
n = int(input("Please enter a number:\n"))
if n == 1:
    print("%d is prime number " %n)
else:    
    for i in range(2,n):
        if n % i == 0:
            print("%d isn't prime number " %n)
            break
    else:
        print("%d is prime number " %n)