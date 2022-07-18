#求一个3*3矩阵主对角线元素之和。
#程序分析：利用双重for循环控制输入二维数组，再将a[i][j]累加后输出
a=[]
for i in range(0,3):
    a.append([]) # 3 4 5行等价于 a=[[],[],[]]
    for j in range(0,3):
        a[i].append(float(input("请输入矩阵第%d行的第%d个元素："%(i+1,j+1))))
print ("该矩阵的对角线元素之和为%f"%(a[0][0]+a[1][1]+a[2][2]))
'''
定义二维数组的两种方式：
方法一：
a=[]
for i in range(0,3):
    a.append([])
    for j in range(0,3):
        a[i].append(float(input("请输入第%d个列表中的第%d行的第%d个元素："%(i,j))))
print (a)
方法二：
a=[[],[],[]]
for i in range(0,3):
    for j in  range(0,3):
        a[i].append(float(input("请输入第%d个列表的的第%d个元素："%(i,j))))
print (a)
'''
