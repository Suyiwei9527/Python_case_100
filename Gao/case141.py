#希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。是非稳定排序算法。先将整个序列分割成为若干子序列分别进行直接插入排序，待整个序列"基本有序"时，再对全体记录进行依次直接插入排序。
import random
l = []
for i in range (15):
    l.append(random.randint(0,100))
print(l)
def ShellSort(l):
    n = len(l)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap,n):#i表示当前待插入的元素，通过内层while循环将其插入到合适的位置
            index = i - gap#index为当前元素在其子序列比较的前一个元素
            Curnum = l[i]
            while index >= 0 and Curnum < l[index]:
                l[index + gap] = l[index]
                index -= gap
            l[index + gap] = Curnum
        gap = gap // 3
    return l
print(ShellSort(l))