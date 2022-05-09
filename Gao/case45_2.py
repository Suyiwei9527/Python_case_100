def Sum(n):
    Sn = 0
    for i in range(n+1):
        Sn += i
    print("The sum is %d" %Sn)
Sum(int(input("I want to calculate the sum of one to:" )))