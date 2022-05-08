#计算 n 个自然数的立方和
n = int(input("Please input a number:\n"))
s = 0
for i in range (1,n+1):
    s += i ** 3
print(s)