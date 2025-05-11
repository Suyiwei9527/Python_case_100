#bubble、去重且排序、快速排序、直接插入排序、希尔排序、简单选择排序、字符串不含重复字符的最长字串长度
import random
import sys
l = []
for i in range(15):
    l.append(random.randint(0 ,100))
print(l)
def sheelsort(l):
    gap = 1
    n = len(l)
    while gap < gap // 3:
        gap = gap * 3 +1
    while gap > 0:
        for i in range(gap ,n):
            minindex = i - gap
            current = l[i]
            while minindex >= 0 and current < l[minindex]:
                l[minindex + gap] = l[minindex]
                minindex -= gap
            l[minindex + gap] = current
        gap //= 3
    return l
print(sheelsort(l))