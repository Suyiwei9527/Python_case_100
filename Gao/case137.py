#选择排序（Selection sort）先在未排序列中找到最小（大）元素放到起始，再继续寻找最小（大）元素，放到已排序序列的末尾。
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def selectsort(l):
    for i in range(len(l)-1):#i为已排好序列的最小值
        minIndex = i#引入minIndex放未排序里最小的值
        for j in range(i+1,len(l)):
            if l[j] < l[minIndex]:
                minIndex = j#找到最小值
        l[minIndex],l[i]=l[i],l[minIndex]#找到的最小值放到外循环最小值的位置
    return l
print(selectsort(l))