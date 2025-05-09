import socket
import struct
import threading
import time
'''
health dbserver "diysql" "Gaov" "gaov" "Arraynetworks777" "SELECT * from runoob_tbl where runoob_id=4;" "Py" 1 2
490000000a382e342e34008d7d75037c46377d2838665900ffffff0200ffdf15000000000000000000000e09073961586779727f12010063616368696e675f736861325f70617373776f726400
020000020103
1000000300000002400000000701050447616f76
010000010740000002036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c0972756e6f6f625f69640972756e6f6f625f69640c3f000b00000003034200000046000003036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c0c72756e6f6f625f7469746c650c72756e6f6f625f7469746c650cff0090010000fd011000000048000004036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c0d72756e6f6f625f617574686f720d72756e6f6f625f617574686f720cff00a0000000fd01100000004c000005036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c0f7375626d697373696f6e5f646174650f7375626d697373696f6e5f646174650c3f000a0000000a800000000038000006036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c05656d61696c05656d61696c0cff00fc030000fd000000000042000007036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c0a62697274685f646174650a62697274685f646174650c3f000a0000000a800000000040000008036465660447616f760a72756e6f6f625f74626c0a72756e6f6f625f74626c096d6f72655f63686172096d6f72655f636861720cff00fcff0300fc100000000030000009013414e5ada6e4b9a020507974686f6e2472776179275c0a52554e4f4f422e434f4d0a323031362d30332d3036fbfbfb0700000afe000002000000
'''
msg1 = b'''I\x00\x00\x00\n8.4.4\x00\x8d}u\x03|F7}(8fY\x00\xff\xff\xff\x02\x00\xff\xdf\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\t\x079aXgyr\x7f\x12\x01\x00caching_sha2_password\x00'''
msg2 = b'''\x02\x00\x00\x02\x01\x03'''
msg3 = b'''\x10\x00\x00\x03\x00\x00\x00\x02@\x00\x00\x00\x07\x01\x05\x04Gaov'''
msg4 = b'''\x01\x00\x00\x01\x07@\x00\x00\x02\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\trunoob_id\trunoob_id\x0c?\x00\x0b\x00\x00\x00\x03\x03B\x00\x00\x00F\x00\x00\x03\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\x0crunoob_title\x0crunoob_title\x0c\xff\x00\x90\x01\x00\x00\xfd\x01\x10\x00\x00\x00H\x00\x00\x04\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\rrunoob_author\rrunoob_author\x0c\xff\x00\xa0\x00\x00\x00\xfd\x01\x10\x00\x00\x00L\x00\x00\x05\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\x0fsubmission_date\x0fsubmission_date\x0c?\x00\n\x00\x00\x00\n\x80\x00\x00\x00\x008\x00\x00\x06\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\x05email\x05email\x0c\xff\x00\xfc\x03\x00\x00\xfd\x00\x00\x00\x00\x00B\x00\x00\x07\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\nbirth_date\nbirth_date\x0c?\x00\n\x00\x00\x00\n\x80\x00\x00\x00\x00@\x00\x00\x08\x03def\x04Gaov\nrunoob_tbl\nrunoob_tbl\tmore_char\tmore_char\x0c\xff\x00\xfc\xff\x03\x00\xfc\x10\x00\x00\x00\x000\x00\x00\t\x014\x14\xe5\xad\xa6\xe4\xb9\xa0 P'''
msg5 = b'''ython$rway'\\\nRUNOOB.COM\n2016-03-06\xfb\xfb\xfb\x07\x00\x00\n\xfe\x00\x00\x02\x00\x00\x00'''
def handle_client(conn, addr):
    print(f"New connection from {addr[0]}:{addr[1]}")
    conn.send(msg1)
    while True:
        try:
            data = conn.recv(1024)
        except:
            print(f"{addr[0]}:{addr[1]} resets the connection")
            return()
        if not data:
            break
        #print(f"receives: {data.decode()}")
        #time.sleep(1)### 延时响应
        #conn.shutdown(socket.SHUT_WR)
        conn.send(msg2)
        time.sleep(0.1)
        conn.send(msg3)
        time.sleep(2)
        conn.send(msg4)
        time.sleep(3)
        conn.send(msg5)       
        #time.sleep(10)
        #conn.close()
        conn.shutdown(socket.SHUT_WR)#FIN

    conn.close()
    print(f"Connection from {addr[0]}:{addr[1]} closed")

def main():
    host = "172.17.10.150"
    #host = "192.168.101.75"
    port = 803

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))### close the connection by reset
    server.bind((host, port))
    server.listen(5)

    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        #conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))### close the connection by reset
        #conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 1))
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()

if __name__ == "__main__":
    main()
