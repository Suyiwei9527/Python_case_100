from scapy.all import *
import random
import time
#sport = 5003
sport = random.randint(10000, 65535)
dport = 78
dstaddr = '172.17.1.47'
TOptional = [(1, b''), (3, b'\x02'), (1, b''), (1, b''), (8, b'\xa6A\x00\x00\x00'), (4, b''), (30, b'\xa6A\x00\x00\x00\x01')]
seq = random.randint(0, 2**32-1)
#产生SYN包（FLAG = S 为SYN）
ret = sr(IP(dst=dstaddr)/TCP(dport=dport,sport=sport,flags='S',seq=seq), verbose = False)
#ret = sr(IP(dst=dstaddr)/TCP(dport=dport,sport=sport,flags='S',seq=seq,options=TOptional), verbose = False)
#响应的数据包产生数组([0]为响应，[1]为未响应)
list = ret[0].res
#第一层[0]位第一组数据包
#第二层[0]表示发送的包，[1]表示收到的包
#第三层[0]为IPv6信息，[1]为TCP信息，[2]为TCP数据
tcpfields_synack = list[0][1][1].fields

sc_sn = tcpfields_synack['seq'] + 1 #随机值
cs_sn = tcpfields_synack['ack']#18
sc_sn_1 = cs_sn + 1072
cs_sn_1 = sc_sn + 2865
sc_sn_2 = cs_sn_1-305

#发送ACK(flag = A),完成三次握手！
send(IP(dst=dstaddr)/TCP(dport=dport,sport=sport,flags='A',seq=cs_sn,ack=sc_sn,options=TOptional), verbose = False)

# 发送数据并记录服务器返回的序列号
data = b'''GET /one.txt HTTP/1.1\r\nHost: www.gdnybank.com\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46\r\nAccept: */*\r\nReferer: http://www.gdnybank.com/grtsckcp/index.html\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6\r\nCookie: ec=dI4tpWfV-1697083379745-31f0123cffd2e464440108; _efmdata=tnRzPlnZ%2F3OMhEWtsmmPsFtYOuIXngYA1%2F9hVnOmtfN%2B6exJopEYlNcUixM2mLVWQh44X7Xz0eQP0RdlW7yRPQ%3D%3D; _exid=yjOvdKUTjjaFeKIpIav2xQc5IP6TbSS9Vl2zjW%2BUrNg%3D; clientlanguage=zh_CN; JSESSIONID=F8EA2925DE031C88891BCB1127C82938; dpyq79XAOQenT=0XvQyJitEyyQTcruMtBwf5LOvz6.BDLu00ijV9kweUNGyL1kjrWawZao3G2efbUxWz5q4pAIT4ElCQ.SkU2GMsTUUh2gsn7dC32VCGDMiKjgtEZISnwRtcOZDMBrikrz_n6Gk_OrQ8UfvGkfJ4KsK9ELpLipleLmnj5bFM1LGBYLJJI0X.7EiwIE6pp4szGDB9DExU68Tav4B4uBHnZYtVOHeZ0M9BJwqeb7MaDT7C8rDfif3u6F7mEhFFMuhww8pTuwDFxtwuwHsQUDo618Ycm4r.TRvv.Wtxnm6FEFGJE34XoLXGgOx93VWY2b3dPxdkmSoAG6BX_MvklL274GMvZC8AZ3eHA_4rpaRztI755W\r\n\r\n'''
data_packet = IP(dst=dstaddr)/TCP(dport=dport, sport=sport, flags='PA', seq=cs_sn, ack=sc_sn)/Raw(load=data)
send(data_packet, verbose=False)
#response = sr(data_packet, verbose=False)
#packets = sniff(count=4, filter="ip4 and tcp")
#for packet in packets:
send(IP(dst=dstaddr)/TCP(dport=dport,sport=sport,flags='A',seq=sc_sn_1,ack=cs_sn_1), verbose=False)
#    send(IPv6(dst='240E:6B9:20::11')/TCP(dport=80,sport=sport,flags='A',seq=sc_sn_1,ack=cs_sn_1), verbose=False)
