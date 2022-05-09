#求1 +2!+3!+...+20!的和。
add=1
for n in range(2,21):
    num=1
    for i in range(2,n+1):
        num=num*i
    add=add+num
print (add)
