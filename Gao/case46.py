#求输入数字的平方，如果平方运算后小于50则退出
def square(x):
    return x * x
print("The program will stop when square is less than 50")
again = True
while again:
    a = int(input("Please enter a integer:"))
    X=square(a)
    print("The square is %d" %X)
    if X < 50:
        again = False
        print("The program stop running")
    else:
        again = True