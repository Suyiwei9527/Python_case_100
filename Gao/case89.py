##加密传递四位的整数：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
l=[]
n = int(input("Please enter a 4-digit number :"))
a = n // 1000
b = (n //100) % 10
c = (n //10)% 10
d = n % 10
l.append(a)
l.append(b)
l.append(c)
l.append(d)
for i in range(4):
	l[i] += 5
	l[i] %= 10
l=reversed(l)
print("".join(str(k) for k in l))