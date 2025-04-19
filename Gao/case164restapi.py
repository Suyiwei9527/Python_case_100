import http.client, urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

datas1 = open('Gao/login.json').read()
datas2 = open('Gao/task.json').read()
#headers = {"content-type": "application/json","Authorization": "Basic Z2FvX3Rlc3Q6MDMwNDU2ODg="}
headers = {"token": "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJhcGkiLCAibm9uY2UiOiAiMTIzNDY1NzI2MzMyMTNBQkMiLCAiZXhwIjogMTczMzc2ODMwMy4xNTc4MSwgImlhdCI6IDE3MzM3NjgwMDMuMTU3ODU1fQ.AyxIp9nRwqtYsSmsciW5rNloi9GzxkpKQ2B1WMM945U"}
conn = http.client.HTTPSConnection("192.168.101.94:9527")
#conn.request("POST", "/checkapi/gettoken", datas1, headers)
conn.request("POST", "/checkapi/gettoken", datas1)
response = conn.getresponse()
print (response.read())
conn.request("POST", "/checkapi/notifyexcution", datas2, headers)
response2 = conn.getresponse()
print (response2.read())