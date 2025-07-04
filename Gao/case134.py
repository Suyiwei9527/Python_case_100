#插入排序通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
def insertionSort(arr):
    for i in range(len(arr)-1):
        preIndex = i
        current = arr[i+1]#当前待插入元素
        while preIndex >= 0 and current < arr[preIndex] : # 如果当前元素小于等于前一个元素，则将前一个元素后移
            arr[preIndex + 1] = arr[preIndex]#为待插入的元素腾出位置
            preIndex -= 1#往前移动
        arr[preIndex + 1] = current#将当前元素插入到腾出的位置
    return arr
print(insertionSort(l))