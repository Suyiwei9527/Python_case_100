"""五人捕鱼,A可将鱼分为五份,多余的一条扔掉,拿走一份
B再将剩下的鱼分为五份,扔掉多余的一条,拿走一份
C、D、E可同样操作,则他们至少捕了几条鱼"""
a = 1 #最后剩的
m = 1 #总共的鱼
n = 0
while n < 6:
    a = m  #第一次剩的就是总共的
    for i in range(5):
        if (a - 1) % 5 == 0:
            a = (a - 1) // 5 * 4
            n += 1
        else:
            n = 0
            break
    if n == 5:
        print(m)
        break
    m += 1