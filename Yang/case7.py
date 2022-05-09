#输出 9*9 乘法口诀表。
for i in range(1,10):
    print('\n')
    for j in range(1,i+1):
        print  ("%d*%d=%d"%(j,i,i*j),end=" ")  #参数end=，规定了输出内容结尾输出什么，默认是换行
