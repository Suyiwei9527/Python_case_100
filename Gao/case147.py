#整数与IP地址互转
import socket
import struct
import random
a = socket.inet_ntoa(struct.pack(">I",random.randint(2164260864,3741648133)))
print(a)