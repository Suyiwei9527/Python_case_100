#键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个#为止
n = input("Please input a str:")
f = open("D:\\test.txt" , "w")
for k in n:
    if k != "#":
        f.write(k)
    else:
        break