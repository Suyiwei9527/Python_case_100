import http.client, urllib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#datas = open('Gao/apv.json').read()
datas = (b'\xfa`\x01 \x00\x01\x00\x00\x00\x00\x00\x01\x03gao\x06knight\x03com\x00\x00\x01\x00\x01\x00\x00)\x10\x00\x00\x00\x00\x00\x00\x00')
headers = {"Accept": "application/dns-message","Content-Type": "application/dns-message"}
conn = http.client.HTTPSConnection("192.168.101.98:443")
conn.request("POST", "/dns-query", datas, headers)
response = conn.getresponse()
print (response.read())