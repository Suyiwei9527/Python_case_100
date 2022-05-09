n=1
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
list_out=[]
i=1
cnt = 0
#for i in list:
while i in list :
    if len(list_out) > 14:
        break
    flag=0
    for j in list_out:
        if i==j:flag=1
    if flag==1:
        i += 1 #i = 9,j = 9时永远在循环，因此需要i = 10,i=30的时候+1会跳出循环
        if i > 30:i=1
        continue
    while len(list_out)<15 : #这个循环应该在最外面
        if n!=9: 
            n=n+1
        elif n==9:
            list_out.append(i)
            n=1
        break
    i += 1
    if i > 30:
        i = 1
print (list_out)