#有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
a=2
list1=[1,3,5,6,8]
i=0
#if elif 和else语句用来判断列表原来的排序规律，递减、递增还是列表元素全部相等
if list1[0]>list1[len(list1)-1]:
    while(i<len(list1)-1):
        if list1[i+1]<a<list1[i]:
            list1.insert(i+1,a) #insert语句在列表特定位置插入元素，被插入的位置原来的元素以及后面的元素依次往后移动
            break
elif list1[0]<list1[len(list1)-1]:
    while(i<len(list1)-1):
        if list1[i]<a<list1[i+1]:
            list1.insert(i+1,a)
            break
else:list1.append(a)
print (list1)