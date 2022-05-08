#打印出杨辉三角形（要求打印出10行如下图）
a=[]
for i in range (10):
    a.append([])
    for j in range(i + 1):
        a[i].append(0)
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1
for i in range(2,10):#第三行开始出去前后两项的值
    for j in range(1,i):
        a[i][j]=a[i-1][j-1] + a[i-1][j] #核心表达式
for i in range (10):#打印出每一个[]的值
    print()
    for j in range(i + 1):
        print(str(a[i][j]) , end=" ")