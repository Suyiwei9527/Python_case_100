#给定一个字符串的时间，将其转换为时间戳
#time.strptime() 根据指定格式，获取结构化时间
#time.mktime() 根据结构时间，获取时间戳
#time.strftime() 根据结构时间，获取指定格式时间
import time
t = "2022-03-12 23:43:00"
timeArray = time.strptime(t,"%Y-%m-%d %H:%M:%S")
timeStamp = time.mktime(timeArray)
print(timeStamp)
a2 = "2022/03/12 23:43:00"
timeArray = time.strptime(a2,"%Y/%m/%d %H:%M:%S")
timeother = time.strftime("%Y/%m/%d %H:%M:%S",timeArray)
print(timeother)
