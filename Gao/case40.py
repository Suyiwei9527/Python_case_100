#将一个数组逆序输出
l=[1,2,3,4,5,6,7,8,9]
for i in range (len(l)//2):
    l[i],l[-i-1]=l[-i-1],l[i]
print(l)