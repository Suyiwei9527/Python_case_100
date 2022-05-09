#
import socket
import random
import struct

#socket.inet_ntoa(struct.pack(">I",ip))
m=socket.inet_ntoa(struct.pack(">I",4294967295))
#p=struct.pack(">I",0xffffffff)
n1=struct.unpack(">I", socket.inet_aton("192.0.0.0"))
n2=struct.unpack(">I", socket.inet_aton("223.255.255.255"))
m1=struct.unpack(">I", socket.inet_aton("128.0.0.0"))
m2=struct.unpack(">I", socket.inet_aton("191.255.255.255"))
print(n1,n2)
print(m1,m2)