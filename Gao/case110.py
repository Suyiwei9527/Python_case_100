#n!=1×2×3×...×n,factorial
n = int(input("Please input a number:\n"))
m = 1
if n < 0:
    print("Please input a number more than 10.")
elif n == 0:
    print("0 factorial is 1")
else:
    for i in range (1,n+1):
        m *= i
    print(m)