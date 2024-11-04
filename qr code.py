import png
from pyqrcode import QRCode
import pyqrcode


s = input("enter some thing: ")

d = "qrcde" + ".png"

url=pyqrcode.create(s)
url.show()
url.png(d,scale=6)
