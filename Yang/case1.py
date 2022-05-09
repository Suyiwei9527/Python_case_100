#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
a_list=[]
for i in range(1,5):
    a=i*100
    for j in range(1,5):
        if i!=j:a=a+j*10
        else: continue
        for k in range(1,5):
            if k!=i and k!=j:
                a=a+k
                a_list.append(a)
                print (a)
            else:continue
print (len(a_list))

