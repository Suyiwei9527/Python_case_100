#if 语句判断数字
while True:
    try:
        n = int(input("Please input a number:"))
        if n > 0:
            print("This is a positive number.")
        elif n < 0:
            print("This is a negative number.")
        else:
            print("this is 0.")
        break
    except ValueError:
        print("You need input a number.")