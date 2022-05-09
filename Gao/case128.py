#使用正则表达式来获取字符串的 URL
import re
str = "：https://www.runoob.com，test://https://www.google.com"
result = re.findall('https?://[a-zA-Z]{3}\.[a-zA-Z]+\.com',str)
print(result)