#二分查找,适用于有规律的list，每次从中间开始查找逐渐缩小范围
l = [11,22,33,44,55,66,77,88,99,100,101]
def binarysearch(l,d):
    s = 0
    i = 0 
    n = len(l)
    while l[i]!=d:
        i = (n - s) // 2 + s
        if l[i] < d:
            s = i
        elif l[i] > d:
            n = i + 1
    return i
print(binarysearch(l,101))