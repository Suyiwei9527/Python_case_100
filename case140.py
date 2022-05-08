#计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def CountingSort(l):
    bucket = []
    for i in range(max(l)+1):
        bucket.append(0)
    for k in l:
        bucket[k] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            l[i] = j
            bucket[j] -= 1
            i += 1
    return l
print(CountingSort(l))