#输入数字检测是否为阿姆斯特朗数:一个n位正整数等于其各位数字的n次方之和,例如1^3 + 5^3 + 3^3 = 153。
n = int(input("Please input a number:\n"))
m = len(str(n))
temp = n
sum = 0
while temp > 0: 
    s = temp % 10
    sum += s ** m
    temp //= 10
if sum == n:
    print("%d is a Armstrong number."%n)
else:
    print("%d is not a Armstrong number."%n)