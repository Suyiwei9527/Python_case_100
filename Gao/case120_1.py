"""30 个人在一条船上,需要 15 人下船,排成一队的位置即为他们的编号,数到 9 的人下船;直到船上仅剩 15 人为止,问下船了人的编号"""
n=1
list=[]
#list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
for i in range(30): #列表生成
    list.append(i+1)
list_out=[]
i=1
while((i in list) and len(list_out)<15):
    flag=0
    for j in list_out:
        if i==j:flag=1
    if flag==1: #and i!=30:
        i=i+1
        if i > 30:i=1
        continue
    #elif flag==1 and i==30:
        #i=1
        #continue
    elif flag==0: #and i!=30:
        if n!=9: 
            n=n+1 
            #i=i+1   
        elif n==9:
            list_out.append(i)
            n=1
    i=i+1
    if i > 30:
        i=1
    #elif flag==0 and i==30:
        #if n!=9: 
            #n=n+1 
            #i=1   
        #elif n==9:
            #list_out.append(i)
            #n=1
            #i=1
print (list_out)