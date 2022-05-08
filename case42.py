#变量作用域
a = 5
def varfunc ():
    a = 2
    print("varfunc internal a forever =%d" %a)
    a += 1
for i in range(5):#a=5 and a=a+5
    print("var is exchange:a = %d" %a)
    a += 3
    varfunc()#varfunc:a=2