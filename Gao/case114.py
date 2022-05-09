#十进制转二进制、八进制、十六进制
n = int(input("Please input a number:\n"))
a = bin(n)
b = oct(n)
c = hex(n)
print(a,b,c)