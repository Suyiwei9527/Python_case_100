import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('172.17.1.48',800))
var=1
while var==1:
    s.send(b'GET / HTTP/1.1\r\n')
    s.send(b'Host:test.com\r\n')
    s.send(b'Upgrade:a')
    time.sleep(5)
    s.send(b'h2c\r\n\r\n')
s.close()