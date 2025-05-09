#快速排序使用分治法（Divide and conquer）把一个list分为较小和较大的2个子序列，然后递归地排序两个子序列
import random
l = []
for i in range (15):
    l.append(random.randint(1,100))
print(l)
def partition(l,left,right):
    key = left
    while(right > left):
        while(right > left and l[right] >= l[key]):
            right -= 1
        while(right > left and l[left] <= l[key]):
            left += 1
        l[left],l[right] = l[right],l[left]
    l[left],l[key] = l[key],l[left]#基准正确的位置，保证左侧都小于基准，右侧都大于基准
    return left
def quicksort (l,left,right):
    if left >= right:
        return
    mid = partition(l,left,right)
    quicksort(l,left,mid-1)
    quicksort(l,mid+1,right)
def Quicksort(l):
    n = len(l) - 1
    quicksort(l,0,n)
    return l
print(Quicksort(l))