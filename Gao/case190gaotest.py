import dns.message
import dns.query

# 创建DNS请求消息
request = dns.message.make_query('example.com', dns.rdatatype.ANY)

# 添加多个域名到Additional Record
additional_record = dns.rdataset.from_text(dns.rdataclass.IN, dns.rdatatype.A, 'additional1.example.com')
additional_record.add(dns.rdataset.from_text(dns.rdataclass.IN, dns.rdatatype.A, 'additional2.example.com'))

# 将Additional Record添加到请求消息中
request.additional.append(additional_record)

# 发送DNS请求
response = dns.query.tcp(request, '8.8.8.8')  # 使用Google Public DNS服务器进行示例查询

# 处理响应
if response:
    print(response)
    # 进行其他响应处理操作
else:
    print("无响应")