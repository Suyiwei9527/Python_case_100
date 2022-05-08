#斐波那契数列是 0, 1, 1, 2, 3, 5, 8, 13
n = int(input("Please input a number:\n"))
l=[0 for i in range(n)]
l[0]=0
l[1]=1
for i in range(2,n):
    l[i]=l[i-1]+l[i-2]
print(l)