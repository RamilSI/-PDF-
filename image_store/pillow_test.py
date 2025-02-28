import os, sys
from PIL import Image

SOURSE_DIR = 'images/'
p1 = Image.open(SOURSE_DIR + '6.10.24 001.jpg')
print(p1.size)
print(p1.mode)
print(p1.format)
print(p1.info)
p1.show()

p2 = Image.open(SOURSE_DIR + 'copy_.png')
p2.show()

x, y = p1.size

p1.paste(p2, (int(x/2), int(y-500)))
p1.show()

# im.draft("L", (100, 100))
# print("draft =", im.mode, im.size)
# im.show()
