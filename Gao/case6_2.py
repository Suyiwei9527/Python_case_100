#斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34...输出n个fib
def fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(n-2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib(10))