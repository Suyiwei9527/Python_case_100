#判断101-200之间有多少个素数，并输出所有素数

import math
count = 100
leap = 1
for i in range (3,20123123123432143243243532):
    k=int(math.sqrt(i + 1))
    for j in range(2,k + 1):
        if i % j == 0:
            leap = 0
            break
    if leap == 0:
        count -= 1
    if leap == 1:
        print('the number:%d is Prime number' % i)
        #count += 1
        #if count % 10 == 0:
            #print('')
    #print(leap)            
    leap = 1            
print('the total is %d' % count)