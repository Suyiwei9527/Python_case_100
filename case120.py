"""30 个人在一条船上,需要 15 人下船,排成一队的位置即为他们的编号,数到 9 的人下船;直到船上仅剩 15 人为止,问下船了人的编号"""
l=[]
for i in range(30):
    l.append(i+1)
m=0
k=0
i=0 
while m < 15:
    if l[i] != 0:k += 1
    if k == 9:
        l[i] = 0
        k = 0
        m += 1
    i += 1
    if i > 29:
        i = 0
for i in range(30):
    if l[i]==0:
        print(i+1,end=" ") 