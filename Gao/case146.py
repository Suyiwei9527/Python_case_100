#urllib
from urllib.request import urlopen
myURL = urlopen("https://www.runoob.com/")
f = open("test.html","wb")
file = myURL.read()
f.write(file)
f.close()