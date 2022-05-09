#定义一个整型数组，并将指定个数的元素翻转到数组的尾部
import random
def reverse_arr(arr,d,n):
    return(left_arr(arr,d))
def left_arr(arr,d):
    temp = 0
    for j in range (d):
        for i in range(n): 
            if i == 0:
                temp = arr[0]
            if i == n-1:
                arr[i] = temp
            else:
                arr[i] = arr[i+1]
    print(arr)
n = int(input("Please input your arr's len:\n"))
d = int(input("Please input your left_reverse number:\n"))
arr = []
for i in range(n):
    arr.append(random.randint(1,100))
print(arr)
reverse_arr(arr,d,n)