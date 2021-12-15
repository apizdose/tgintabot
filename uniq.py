import random
from PIL import Image, ImageFilter
import glob


def tspose(filename):
    im = Image.open(filename)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    pix = [(pixel[0], pixel[1], pixel[2]) for pixel in im.getdata()]
    for i in range(100):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255) 

        ran=random.randint(10,(len(pix) - 10))

        pix[ran] = (red, green, blue)

    im.putdata(pix)
    im.save(filename)
    

mkfiles = glob.glob("*.jpg")

for i in mkfiles:
    tspose(i)
