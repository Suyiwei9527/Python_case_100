import http.client, urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

datas = open('Gao/apv.xml').read()
headers = {"content-type": "text/xml"}
conn = http.client.HTTPSConnection("[192::100:6319]:10086")
conn.request("POST", "/cgi-bin/xmlrpc_server", datas, headers)
response = conn.getresponse()
print (response.read())