#对10个数进行排序。
#_*_coding:utf-8_*_
def mao_pao_order(list):
    flag=1
    while flag==1:
        flag=0
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]#使用这个命令等价于下面三行命令，该命令也不会导致给list[i+1]赋值list[i]的时候list[i]已经被赋值为list[i+1]
                #a=list[i]
                #list[i]=list[i+1]
                #list[i+1]=a
                flag=1
    print(list)
list1=[1,3,5,2,34,23,56,78,12,3]
mao_pao_order(list1)