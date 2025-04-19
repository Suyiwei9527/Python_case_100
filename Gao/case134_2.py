#插入排序通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def insertionsort(l):
    for i in range (len(l)-1):
        current = l[i+1]#待排的数
        preindex = i
        while preindex >= 0 and current < l[preindex]:#比current大的向后移动
            l[preindex+1] = l[preindex]
            preindex -= 1
        l[preindex+1] = current#待排的数更大的话插入到正确位置
    return l
print(insertionsort(l))