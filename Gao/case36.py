#求100之内的素数
x=[]
for i in range (2,101):
    for s in range (2,i):
        if i % s == 0:
            break
    else:
        x.append(i)
print(x)