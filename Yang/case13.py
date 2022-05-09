#打印出所有的其各位数字立方和等于该数本身的数。例如：153，153=1的三次方＋5的三次方＋3的三次方
for i in range (0,99999):
    #获取i的位，个位十位百位等
    j=i    
    wei_list=[]
    while(j>0):
        wei=j%10
        wei_list.append(wei)
        j=int(j/10)
    lifanghe=0
    #算立方和
    for w in wei_list:
        lifanghe=lifanghe+w*w*w
    #判断  输出
    if lifanghe==i:print(i,end=' ')
