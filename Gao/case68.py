#有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
n = int(input("Please enter the total of numbers:"))
m = int(input("Please enter change numbers:"))
def move (l,n,m):#关键步骤
	l_end=l[-1]
	for i in range(n-1,-1,-1):
		l[i]=l[i-1]
	l[0] = l_end
	m -= 1
	if m >0:
	    move(l,n,m)
l=[]
for i in range(n):
    l.append(int(input("Please enter your number:")))
print("the raw list is:",l)
move(l,n,m)
print("the after list is:",l)