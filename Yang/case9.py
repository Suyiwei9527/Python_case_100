#暂停一秒输出，并格式化当前时间
import time
from datetime import datetime
time.sleep(1)
#以下两种方式为输出格式化的当前本地时间最简单的import time的方法方式
print(time.asctime(time.localtime(time.time())))
print(time.ctime(time.time()))
#以下方式为输出格式化的当前本地时间最简单的import localtime的方法
print(datetime.now())