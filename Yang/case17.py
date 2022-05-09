#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#思路：找到目标（正则），计数（）
from typing import Counter
import re
input='ASDgfrf   %%%%@#'
#找到所有英文字母--计算数量
str_list=re.findall('[a-zA-z]',input)#!!!!findall:配 返回为列表。
print('number of string is %d'%len(str_list))#!!!!len（）：返回容器（eg列表 字符串）的对象个数，
#找到所有空格--计算数量
space_list=re.findall(' ',input)
print('number of space is %d'%len(space_list))
#找到所有其他字符--计算数量
other_list=re.findall('[^a-zA-z ]',input)
print('number of other string is %d'%len(other_list))