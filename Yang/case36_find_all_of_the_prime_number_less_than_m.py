#输出100以内的所有素数
#判断n是否为素数的函数，是的话返回n
def prime_number(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return(n)
#返回m以内所有素数的函数，
def find_all_of_prime_number_less_than_m(m):
    list_prime_number=[]
    for i in range(3,m):
        if prime_number(i) :list_prime_number.append(prime_number(i))
    return (list_prime_number)
#调用find_all_of_prime_number_less_than_m函数
print(*find_all_of_prime_number_less_than_m(100),end='')# 1. list为列表，print(*list)表示输出列表的所有元素,直接写print(list)输出结果里面有[] 2. end='' 表示不已什么结尾，不写的话默认以换行结尾
print("是100以内的素数")