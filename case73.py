#反向输出一个链表,reverse
def func_lb ():
    l=[]
    n=int(input("Please input the number:"))
    for i in range(n):
        l.append(str(input("Please enter a alpha:")))
    print(l)
    l.reverse()
    print(l)
func_lb()