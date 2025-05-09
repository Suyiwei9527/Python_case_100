# -*- coding: utf-8 -*-
import time
import socket
import struct
import os


#message = b'''GET /bug/bug0607_9.txt HTTP/1.1\r\nHost: 172.17.1.148\r\nAuthorization: Basic Z2FvdjoxMjM0NTYx\r\nUser-Agent: curl/7.85.0\r\nAccept: */*\r\n\r\n'''
message1 = b'''GET /gao.php HTTP/1.1\r\nHost: 172.17.1.148\r\nAuthorization: Basic Z2FvdjoxMjM0NTYx\r\nAccept: */*\r\n\r\n'''
message = b'''GET /gao.php HTTP/1.1\r\nHost: 172.17.1.148\r\nConnection: Keep-Alive\r\nAccept: */*\r\n\r\n'''
message4 = b'''abcdef'''
message5 = b'''POST /gao.php HTTP/1.1\r\nHost: 172.17.8.245\r\nUser-Agent: curl/8.2.1\r\nAccept: */*\r\nContent-Length: 1106\r\nContent-Type: multipart/form-data; boundary=------------------------109718f379664599\r\n\r\n--------------------------109718f379664599\r\nContent-Disposition: form-data; name="filename"; filename="test.html"\r\nContent-Type: text/html\r\n\r\n-----BEGIN PRIVATE KEY-----\nMIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBALdO1ELPSGWtwOEd\nX+zmC7cgeHo/h6+j4mF9wWbx3CCZqF7tLJynZ0SjE3ejDr7LN66UJfTKh59XXpd2\ncVVkY9dl4dabF4hhJkUYFyH3RrpYSaSREV10mnkidkUNih+3DS0dBNig6SSlS3hi\nsPvRn2lf/HWZ6Iw0oMjMoTuzV+irAgMBAAECgYEAkMSS4kiuFo9I2wDF92QfMHtW\nasWttUsqyG/2xASTIrP3wzBwoS+cYRqhj0SZqpj32sppx5AD2BW6QMhr7VKhfe36\nirVcyyuV+smTDhE0qLJp1ZT3WeHZ+gCm4893M3qM0CrSAnYIZx0F3ev0eXCzB4il\n9iyodWxq/xNygSwdmsECQQDtkbSPUhV+5O5mhTKe6tM4HNtRns+hnQdEvuhgsUdb\nzZe9Q9hCWGFPBK0Dz7gAop1/2Dt8IGfvWkTvEifdwb37AkEAxYd05L/CFCzo0DoL\navt+eIyVBePdZqG0kOYj0Cg8NZ32GghqrjkXv/rJvUJmOblC4VTBCGlas/eMWcwH\ntBPxEQJASG0/auJPg1wwAjlhcWmN83F4u617B35kFOVO2wuxAZ/wPtdMOw3OvNRk\nGuFc63SoJ624lOMcTLBsi6YxWT4TuQJBAI4ZNiRhNpMhA5LYTuJ1bbP3HjWQiPOO\nHMGobdcPOtEvg52StHwFImq/VWXLYJLiDZTgTcVpVRDmYpcuydPoDKECQQDeHFU3\nEBjgYRNOstWMrdLQWoseKS51o/fK+7LBkOI8hyDOef8lZIHJlwS4wV5vHApj8KZX\nWM9u8YO1oLIRZPjU\n-----END PRIVATE KEY-----\n\r\n--------------------------109718f379664599--\r\n'''

server_address = ('172.17.8.245', 80)
#server_address = ('192.168.101.75', 802)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))# close the connection by reset
#client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 20))
state = client_socket.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
if state == 0:
    print("套接字状态：正常")
else:
    print(f"套接字状态：异常 ({os.strerror(state)})")



for i in range(1,2):   ##长连接消息多发
    client_socket.sendall(message5)
    data = client_socket.recv(1024)
    print(data.decode())
    time.sleep(3)
client_socket.close()
