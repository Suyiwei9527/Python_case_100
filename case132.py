#给定一个时间戳，将其转换为指定格式的时间
import time
nowtimestamp = time.time() #时间戳，float
nowstructtime = time.localtime(nowtimestamp) #UCT时区的struct_time
otherftime = time.strftime("%Y-%y-%d %H:%M:%S" , nowstructtime)#struct_time 转换为其他格式
print(otherftime)