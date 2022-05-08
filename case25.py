#求1+2!+3!+...+20!的和
l = range(1,21)
def Jc(x):
    r=1
    for i in range (1,x+1):
        r*=i
    return r
s=sum(map(Jc,l))
print("The answer is:%s" %s)