#给一个不多于5位的正整数求它是几位数，逆序打印出各位数字
x = int(input("Please enter a number:"))
if x >99999:
    print("The number must less than 99999")
else:
    a = x // 10000
    b = x % 10000 // 1000
    c = x % 1000 // 100
    d = x % 100 // 10
    e = x % 10
    if a != 0:
        print("The number is five digits",e,d,c,b,a)
    elif b != 0:
        print("The number is four digits",e,d,c,b)
    elif c != 0:
        print("The number is three digits",e,d,c)
    elif d != 0:
        print("The number is two digits",e,d)
    elif e != 0:
        print("The number is one digits",e)