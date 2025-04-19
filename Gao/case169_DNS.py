import socket
import struct

def handle_request(data):
    # 解析DNS请求数据
    # 获取查询ID
    query_id = data[0:2]

    # 获取标志位
    flags = data[2:4]

    # 获取问题数
    qdcount = struct.unpack('!H', data[4:6])[0]

    # 获取查询字符串
    query_str = ''
    i = 12
    while True:
        length = data[i]
        if length == 0:
            break
        query_str += data[i+1:i+length+1].decode('utf-8') + '.'
        i += length + 1
    query_str = query_str[:-1]

    # 构造响应数据
    response = b''
    response += query_id
    response += flags  # 标志位（一般不变）
#    response += b'\x00\x01'  # 问题数
#    response += b'\x00\x01'  # 资源记录数
#    response += b'\x00\x00'  # 授权资源记录数
#    response += b'\x00\x00'  # 额外资源记录数
    response += data[12:]    # 复制查询部分

    # 查询问题，并添加到响应数据中
    answers = get_answers(query_str)
    if answers:
        # 添加响应标记和类型/类别
        response += b'\xc0\x0c'   # 响应标记指向查询部分
        response += b'\x00\x01'   # 响应类型为A记录
        response += b'\x00\x01'   # 响应类别为IN

        # 添加TTL、数据长度和IP地址
        ttl = struct.pack('!I', 60)
        response += ttl
        response += b'\x00\x04'
        response += socket.inet_aton(answers[0])

    return response

def get_answers(query_str):
    # 此处省略查询过程，直接返回固定的本地IP地址
    return ['192.168.100.101']

def main():
    # 创建TCP套接字并绑定到地址和端口
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.100.105', 53))

    # 监听连接请求
    sock.listen(5)

    while True:
        # 接受客户端连接请求
        conn, addr = sock.accept()

        # 读取DNS请求数据
        data = conn.recv(1024)

        # 处理DNS请求并返回响应数据
        response = handle_request(data)

        # 发送DNS响应数据给客户端
        conn.sendall(response)

        # 关闭连接
        conn.close()

if __name__ == '__main__':
    main()
