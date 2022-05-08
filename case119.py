#导入 datetime 模块来获取昨天的日期
import datetime
def getYesterday():
    today=datetime.date.today()
    yesterday=today-datetime.timedelta(days=1)
    return yesterday
print(getYesterday())