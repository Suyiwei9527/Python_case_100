#归并排序（Merge sort，或mergesort）是在归并操作上的一种有效的排序算法,是分治法（Divide and Conquer）的一个非常典型的应用。
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def conquer(l1,l2):
    l_new = []
    for i in range(len(l1)):
        if len(l2) == 0:
            l_new.append(l1[i])
        while len(l2) > 0:
            j = 0
            if l1[i] < l2[j]:
                l_new.append(l1[i])
                if i == len(l1)-1:
                    l_new.extend(l2)
                break
            if l1[i] >= l2[j]:
                l_new.append(l2[j])
                del l2[j]
            if len(l2) == 0:
                l_new.append(l1[i])
                break
    return l_new
def divide(l):
    if len(l) < 2:
        return l
    left = divide(l[0:len(l)//2])
    right = divide(l[len(l)//2:])
    return conquer(left,right)
print(divide(l))