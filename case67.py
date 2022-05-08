#输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
def Max_ch (l):
    max = 0
    for i in range(1,len(l)-1):
        if l[i] > l[max] : max = i
    l[0],l[max]=l[max],l[0]
def Min_ch (l):
    min = 0
    for i in range(1,len(l)-1):
        if l[i] < l[min] : min = i
    l[-1],l[min]=l[min],l[-1]
l=[]
for i in range(6):
    l.append(int(input("please input your number:")))
Max_ch(l)
Min_ch(l)
print(l)