#写一个函数求一个字符串的长度，在main函数中输入字符串，并输出其长度
def func_len(s):
	len = 0
	for i in s:
		len += 1
	print("the string len is :" ,len)
if __name__ == "__main__":
	s = input("please input a string:")
	s_len = func_len(s)