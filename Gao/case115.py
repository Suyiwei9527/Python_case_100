#实现ASCII码与字符相互转换 chr: ord:
a = int(input("Please input a ASCII:\n"))
b = input("Please input a str:\n")
c = chr(a)
print("%d's str is"%a,c)
print(b + "'s ASCII is",ord(b))