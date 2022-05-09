#实现简单计算器实现，包括两个数基本的加减乘除运算
def sum(x1,x2):
    sum = x1 + x2
    return sum
def subtract(x1,x2):
    return x1 - x2
def multiply(x1,x2):
    return(x1 * x2)
def divide(x1,x2):
    return x1 / x2
print("chose fx:")
print("1:+")
print("2:-")
print("3:*")
print("4:/")
choice = input("Please input your fx number:\n")
n1 = int(input("Please input a number:\n"))
n2 = int(input("Please input an another number:\n"))
if choice == "1":
    print(sum(n1,n2))
elif choice == "2":
    print(subtract(n1,n2))
elif choice == "3":
    print(multiply(n1,n2))
elif choice == "4":
    print(divide(n1,n2))