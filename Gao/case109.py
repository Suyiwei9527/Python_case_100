#输出指定范围内的素数
a = int(input("Please input the left number:\n"))
b = int(input("Please input the right number:\n"))
l = []
for n in range(a,b+1):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            l.append(n)
print(l)