#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#sqrt 平方根函数
import math
num = -99
while True:
    if  math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268) - int(math.sqrt(num + 268)) == 0:
        print(num)
        #break
    num +=1