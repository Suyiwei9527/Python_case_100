#堆排序（Heapsort）利用堆这种数据结构所设计的一种排序算法。1.建立大顶堆2.堆顶与数组末尾元素交换3.剩余序列重复建立顶堆交换
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def adjustHeap(l,i,size):
    lchild = 2 * i + 1#非叶子节点的两个子节点
    rchild = 2 * i + 2
    max = i#三个节点中找到最大的元素
    if lchild < size and l[lchild] > l[max]:
        max = lchild
    if rchild < size and l[rchild] > l[max]:
        max = rchild
    if max != i:#当前节点不是最大元素，把最大元素换过来，继续调整堆
        l[max],l[i] = l[i],l[max]
        adjustHeap(l,max,size)#小节点向下调整
def BuildHeap(l):#生成一个堆顶
    for i in range (len(l)//2,-1,-1):
        adjustHeap(l,i,size)#不断调整非叶子节点的堆
def HeapSort(l):#此时堆顶的数最大
    global size
    size = len(l)
    BuildHeap(l)
    for i in range(len(l)-1,0,-1):
        l[0],l[i] = l[i],l[0]#根节点都是最大的数，放到后面
        #size -= 1
        adjustHeap(l,0,i)#交换完后调整堆（size=i表示除去排好的数），只调节根节点
    return l
print(HeapSort(l))