#两个变量值互换
a = int(input("please enter the first number:"))
b = int(input("please enter the second number:"))
print("a=%d,b=%d" %(a,b))
temp = a
a = b
b = temp
print("a=%d,b=%d" %(a,b))