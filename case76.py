#写一个函数，n为偶数调用函数求1/2+1/4+...+1/n,n为奇数调用函数1/1+1/3+...+1/n
def func_s (n):
	Sn = 0
	i=1
	if n % 2 == 0:
		while((2 * i ) <= n):
			Sn += 1/(2 * i )
			i += 1
	else:
		while((2 * i )-1 <= n):
			Sn += 1/((2 * i )-1)
			i += 1
	print(Sn)
if __name__ == "__main__":
	n = int(input("Please enter a number:\n"))
	func_s(n)