#键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个#为止
from re import I
file=open("E:\python\\ff.txt","w")
input_str=input("请输入一些字符：")
for i in input_str:
    if i!="#" :
        file.write(i)
file.close()
