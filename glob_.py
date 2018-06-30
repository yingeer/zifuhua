import glob, os.path
from PIL import Image
import PIL
im = Image.open("images/test.png")
print(im.size, im.mode )
im2=Image.open("images/ascii_dora.png")
newimg1 = Image.new("L", (200, 200), 57)
newimg2=Image.new("RGB", (200, 200), (255, 255, 255))
print(newimg2.mode, newimg2.size)
im2.resize((20, 20)).show()
im3 = im2.copy()
im3.show()
print(help(PIL.Image))
print(im3.getpixel((45,56)))
im3.thumbnail((18, 18))