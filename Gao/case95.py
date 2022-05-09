#字符串日期转换为易读的日期格式
from dateutil import parser
dt = parser.parse("Feb 15 2020 11:09 AM")
print (dt)