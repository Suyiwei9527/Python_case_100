#输出for i in range(3000) 程序运行的时间 
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print (i)
    end = time.time()
 
    print (end - start)