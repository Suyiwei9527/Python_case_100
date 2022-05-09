#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
#持续找最小的因数
def min_factor(a,factor_list):
    for i in range(2,a):
        flag=0
        if a%i==0:
            factor_list.append(i)
            min_factor(int(a/i),factor_list)
            flag=1
            break
    if flag==0:
        factor_list.append(a)
    return factor_list #若把return factor_list写在if里面，因为使用了递归只有在执行最里面的循环时可以返回factor_list，其他循环不满足flag=1都会返回为空，最终返回的是最外面循环的返回值，所以会返回为空。
target=int(input("please input a positive integer:"))
factor_list=[]
print (min_factor(target,factor_list))

