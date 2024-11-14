import os, sys
from PIL import Image

SOURSE_DIR = 'images/'
p1 = Image.open(SOURSE_DIR + '6.10.24 001.jpg')
print(p1.size)
print(p1.mode)
print(p1.format)
print(p1.info)
p1.show()
# ava = p1.crop((660, 650, 1850, 750))
# ava = ava.transpose(Image.Transpose.ROTATE_180)
# ava.save(SOURSE_DIR + 'ava.jpeg')
# ava.show()
# p1.paste(ava, (500, 600))
# p1.show()
p2 = Image.open(SOURSE_DIR + '6.10.24 002.jpg')


im = Image.open(SOURSE_DIR + '6.10.24 001.jpg')
box = Image.open(SOURSE_DIR + 'pechat.png')
im.paste(box, (1200, 2000))

im.draft("L", (100, 100))
print("draft =", im.mode, im.size)
im.show()
