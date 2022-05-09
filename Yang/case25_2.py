#求1 +2!+3!+...+20!的和。
a=1
sum=0
for i in range(1,21):
    a=a*i
    sum=sum+a
print (sum)