#输入三个整数x,y,z，请把这三个数由小到大输出
num = []
for i in range(1,4):
    m = int(input('Please enter the %d integer:' %i))
    num.append(m)
    num_order = sorted(num)
print (num_order)