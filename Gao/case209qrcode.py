import pyqrcode
import png

data = "https://y.qq.com/"
qr = pyqrcode.create(data)
qr.png('img.png', scale=8)