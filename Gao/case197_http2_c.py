import httpx
import asyncio

async def send_http2_request(url, headers):
    # 创建一个异步客户端
    async with httpx.AsyncClient(http2=True) as client:
        # 发送HTTP/2请求
        response = await client.get(url, headers=headers)
        return response

# 自定义请求头
custom_headers = {
    "User-Agent": "My Custom User Agent",
    "Authorization": "Bearer my_token",
    "Custom-Header": "Custom Value"
}

# 创建事件循环并运行异步函数
loop = asyncio.get_event_loop()
response = loop.run_until_complete(send_http2_request("https://192.168.101.88:443/gao.php", headers=custom_headers))

# 打印响应结果
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
