#用户输入一个数字，并计算这个数字的平方根
n = float(input("Please enter a number:\n"))
n_sqrt = n ** 0.5
#print("{0}'s sqrt is {1}" .format(n , n_sqrt))
print("%0.2f's sqrt is %0.2f" %(n , n_sqrt))