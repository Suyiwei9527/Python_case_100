#取一个整数a从右端开始的4〜7位,1 & any = any
a = 9
b = a >> 4
c = ~(~0 << 4)
d = b & c
print(bin(a))
print(bin(d))