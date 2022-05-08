#选择排序（Selection sort）先在未排序列中找到最小（大）元素放到起始，再继续寻找最小（大）元素，放到已排序序列的末尾。
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def selectsort(l):
    l_new = []
    while(len(l) > 0):
        min = l[0]
        for i in range(len(l)):
            if l[i] < min:
                min = l[i]
        l_new.append(min)
        l.remove(min)
    return l_new
print(selectsort(l))