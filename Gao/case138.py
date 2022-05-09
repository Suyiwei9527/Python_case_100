#冒泡排序（Bubble Sort）重复地走访数列，一次比较两个元素改变顺序，直到没有再需要交换停止走访，算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def bubblesort (l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1): #i每走访一次，底部冒泡出一个较大值
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
print(bubblesort(l))