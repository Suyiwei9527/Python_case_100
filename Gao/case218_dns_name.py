import random
import string
import os

def generate_hostname(): # 生成10个随机字符串
    x = random.randint(1, 4)
    #chars = string.digits + string.ascii_letters + "-*/;,/"
    chars = string.digits + string.ascii_letters
    random_string = ''.join(random.choices(chars, k=x))
    hostname = bytes([x-1]) + random_string.encode()
    return hostname
print(generate_hostname())