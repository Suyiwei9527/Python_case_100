#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def a(num,flag):#flag每轮都要更新的数最好作为参数输入，若以第三行的方式书写，flag的值没办法每次开始都会被替换为0，无法更新为上轮结束的值
    #flag=0
    if num>1 :
        flag+=1
        print(int(num%10))
        num=num/10
        a(num,flag)
    else: print("this num have %d digit"%flag)
num1=12354
a(num1,0)