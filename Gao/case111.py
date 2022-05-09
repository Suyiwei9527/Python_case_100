#九九乘法表
for i in range(1,10):
    print()
    for n in range(1,i+1):
        print("%d*%d=%d"%(i,n,i*n),end=" ")