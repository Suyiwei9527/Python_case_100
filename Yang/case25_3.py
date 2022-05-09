#求1 +2!+3!+...+20!的和。
def multiply (a):
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
print(sum(map(multiply,range(1,21))))