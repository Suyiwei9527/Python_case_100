#键盘输入一个字符串，小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
n = input ("Please input a string:\n")
f = open("test.txt" , "w")
f.write(n.upper())
f = open("test.txt" , "r")
m = f.read()
print(m)
f.close