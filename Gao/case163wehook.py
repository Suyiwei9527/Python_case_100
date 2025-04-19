import http.client, urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#datas = open('Gao/apv.xml').read()
datas = "{\"msgtype\":\"text\",\"text\":{\"content\":\"hello world\"}}"
headers = {"content-type": "application/json"}
conn = http.client.HTTPSConnection("qyapi.weixin.qq.com")
conn.request("POST", "/cgi-bin/webhook/send?key=93152ae6-6980-4a34-9d4d-03ef78ce041c", datas, headers)
response = conn.getresponse()
conn.close()
#print (response.read())