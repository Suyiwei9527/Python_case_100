#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#k=[]
#n=-1
for j in range (2, 10):
    n=-1
    k=[]
    s = j
    for i in range (1,j):#（1，j)不包括自己
        if j % i == 0:# 得出j的因子
            n+=1
            s-=i            
            k.append (i)
    if s == 0:
        print (j)
        print (n)
        print (k)
        #for i in range (n):
            #print (str(k[n]))