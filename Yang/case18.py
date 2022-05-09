#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=int(input('please input positive integer a:'))
num=int(input('please input the amount of addend,amount must be positive integer:'))
s=0
if  a<0 or num<0 or type(a)!=int or type(num)!=int:print('input number!')
for i in range(1,num+1):
    addend=0
    for j in range(0,i):
        addend=addend+a*pow(10,j)
    s=s+addend
print (s)
    