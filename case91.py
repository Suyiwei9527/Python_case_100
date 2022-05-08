#time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数
#time.ctime 时间戳（按秒计算的浮点数）转化为time.asctime()的形式
#time.asctime 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串
#time.localtime 函数类似gmtime()，作用是格式化时间戳为本地的时间
#time.gmtime 函数将一个时间戳转换为UTC时区（0时区）的struct_time
if __name__ == '__main__':
    import time
    print (time.time())
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))