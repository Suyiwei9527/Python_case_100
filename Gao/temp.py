import socket
from diameter_parser import parse_diameter_message

def handle_diameter_request(client_socket):
    # 在这里处理Diameter请求
    print("Received Diameter request from", client_socket.getpeername())

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # 解析Diameter消息
        diameter_msg = parse_diameter_message(data)
        # 判断消息类型
        msg_type = get_message_type(diameter_msg)
        if msg_type == "CER":
            # 假设这里是处理CER请求的逻辑
            # 构造CEA报文
            cea_packet = construct_cea_packet()
            # 发送CEA报文
            client_socket.send(cea_packet)
        else:
            # 处理其他类型的Diameter请求
            print("xxxx")

def construct_cea_packet():
    hex_stream = "10000a0000"
    cea_packet = bytes.fromhex(hex_stream)
    return cea_packet


def start_diameter_server():
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 3868))  # 绑定服务器IP和端口
    server_socket.listen(1)  # 监听客户端连接

    print("Diameter server started.")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)
        
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                # 解析Diameter消息
                diameter_msg = parse_diameter_message(data)
                # 处理Diameter请求
                handle_diameter_request(client_socket)
        except Exception as e:
            print("Error occurred:", str(e))
        finally:
            client_socket.close()

start_diameter_server()