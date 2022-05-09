#利用递归方法求5!
def jc(j):
    X = 0
    if j == 0:
        X = 1
    else:
        X = j * jc(j - 1)
    return  X
print (jc(5))