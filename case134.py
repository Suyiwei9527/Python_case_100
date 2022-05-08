#插入排序通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
def insertionsort(l):
    if l[0] > l[1]:
        l[0],l[1] = l[1],l[0]
    l_or = []
    l_or.append(l[0])
    l_or.append(l[1])
    for i in range (len(l)-1,1,-1):
        for j  in range (len(l_or)-1,-1,-1):
            if l[i] >= l_or[j]:
                l_or.insert(j+1,l[i])
                break
            if j == 0:
                l_or.insert(0,l[i])
                break
    return l_or
print(insertionsort(l))