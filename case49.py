#使用lambda来创建匿名函数
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x
if __name__ == "__main__":
    a = 50
    b = 30
    print("The max is:%d" %MAXIMUM(a,b))
    print("The mini is:%d" %MINIMUM(a,b))