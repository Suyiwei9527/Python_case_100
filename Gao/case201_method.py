import random
import string
import os
methods_list = []

for _ in range(10):  # 生成10个随机字符串
    x = random.randint(1, 63)
    #chars = string.digits + string.ascii_letters + "-*/;,/"
    chars = string.digits + string.ascii_letters
    random_string = ''.join(random.choices(chars, k=x))
    msg = bytes([x])
    print(msg)
    methods_list.append(random_string)
print(methods_list)