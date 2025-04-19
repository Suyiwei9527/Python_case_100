import requests

session = requests.Session()

url = 'http://172.17.1.45/bug/bug0612_1.txt'

for i in range(10):
    response = session.get(url)
    print(response.text)