import h2
import asyncio
import socket
from h2.connection import H2Connection

async def send_rst_stream_frame():
    # 创建一个 TCP 连接
    sock = socket.create_connection(("192.168.101.88", 800))

    # 使用 h2 库创建一个连接对象
    conn = h2.connection.H2Connection(client_side=True)

    # 启动连接
    await asyncio.sleep(0.1)  # 等待一段时间以确保连接建立
    data = conn.initiate_connection()
    sock.sendall(data)

    # 发送一个请求
    request_headers = [
        (":method", "GET"),
        (":scheme", "http"),
        (":authority", "192.168.101.88"),
        (":path", "/"),
    ]
    await asyncio.sleep(0.1)  # 等待一段时间以确保连接建立
    data = conn.send_headers(1, request_headers, end_stream=False)
    sock.sendall(data)

    # 接收响应
    while True:
        data = sock.recv(4096)
        events = conn.receive_data(data)
        for event in events:
            if isinstance(event, h2.events.ResponseReceived):
                print(f"Received response: {event.headers}")
            elif isinstance(event, h2.events.StreamEnded):
                print("Stream ended")
                # 在此处发送 RST_STREAM 帧
                data = conn.reset_stream(event.stream_id)
                sock.sendall(data)
            elif isinstance(event, h2.events.ConnectionTerminated):
                print("Connection terminated")
                return

asyncio.run(send_rst_stream_frame())