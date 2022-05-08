#利用递归，将所输入的5个字符，以相反顺序打印出来
def output(s,l):
    if l == 0:
        return
    print(s[l-1],end=" ")
    output(s,l-1)
c = str(input("Please enter a string:"))
l = len(c)
output(c,l)