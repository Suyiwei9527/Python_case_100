#输入3个数a,b,c，按大小顺序输出
l=[]
for i in range(3):
    l.append(int(input("please input a number:")))
def swap (p1,p2):
    return p2,p1
if l[0] > l[1] : l[0],l[1] = swap(l[0],l[1])
if l[0] > l[2] : l[0],l[2] = swap(l[0],l[2])
if l[1] > l[2] : l[1],l[2] = swap(l[1],l[2])
print(l)