#输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
a = int(input("Please enter a odd number:\n"))
if a%2==0: print("Please enter a odd number,this number isn't odd number!")
else :
    b=9
    count=1
    while ( b%a != 0):
        b=b*10+9
        count=count+1
    print("%d个9" %count)