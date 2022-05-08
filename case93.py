#perf_counter()返回当前的计算机系统时间,需要调用两次计算差值来统计程序运行时间
if __name__ == '__main__':
    import time
    start = time.perf_counter()
    for i in range(10000):
        print (i)
    end = time.perf_counter()
    print ('different is %6.3f' % (end - start))