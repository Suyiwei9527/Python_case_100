#计算几天前时间并转换为指定格式
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
print(yesterday.strftime("%Y/%m/%d %H:%M:%S"))