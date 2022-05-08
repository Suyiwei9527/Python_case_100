#输入某年某月某日，判断这一天是这一年的第几天
import datetime
import time
dtstr = str(input('Enter the datetime:(20210629):'))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:3] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print(dt)
print(another_dt)
print(dt-another_dt)
print(int((dt-another_dt).days) + 1)