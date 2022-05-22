#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def output(list,l):
    if l==0:print(list[0])
    else :
        print(list[l])
        output(list,l-1)
list1=input('please input five characters:')
l1=len(list1)-1
output(list1,l1)