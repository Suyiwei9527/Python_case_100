#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
num=0
def feb(n):
    if n==1 or n==2: return 1
    else: return feb(n-1)+feb(n-2) 
for j in range(2,22):
    a=feb(j+1)
    b=feb(j)
    num=num+a/b
print (num)
#print("sum of first 20 number is %f " %num)