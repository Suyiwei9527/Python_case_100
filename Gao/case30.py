#判断一个数是否为回文数，12321是回文数
a = int(input("Please enter a five-digit number:\n"))
x = str(a)
flag = 1
for i in range(len(x)//2):
    if x[i] != x[-i-1]:
        flag = 0
        break
if flag == 0:
    print("%d is not a Palindrome " %a)
else:
    print("%d is a Palindrome " %a)