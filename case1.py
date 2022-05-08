#1 2 3 4四个数字，可组成多少个互不相同无重复的三位数，分别是哪些
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and k!=j:
                print(i*100+j*10+k)
                count+=1
print ('The total count is:%d' % count)