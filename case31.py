#仅输入一个字母判断是星期几
x = input("Please enter an alpha:\n")
if x == 's':
    x = input("Please enter the second alpha:\n")
    if x == 'u':
        print ("Today is Sunday")
    elif x == 'a':
        print ("Today is Saturday")
    else:
        print ("Your alpha is error")
elif x == 'f':
    print ("Today is Friday")
elif x == 't':
    x = input("Please enter the second alpha:\n")
    if x == 'h':
        print ("Today is Thursday")
    elif x == 'u':
        print ("Today is Tuesday")
    else:
        print ("Your alpha is error")
elif x == 'w':
    print ("Today is Wednesday")
elif x == 'm':
    print ("Today is Monday")
else:
    print("Your alpha is error")