import PIL
from PIL import Image
import os
import sys

img = Image.open("x.jpg")

def xpand (img):
    height, width = img.size
    new_im = Image.new('RGB', img.size)
    halfx = int(new_im.size[0]/2)
    halfy = int(new_im.size[1]/2)
    img = img.resize((halfx, halfy),)
    
    og = img
    ud = img.transpose(Image.FLIP_TOP_BOTTOM)
    lr = img.transpose(Image.FLIP_LEFT_RIGHT)
    lrud = lr.transpose (Image.FLIP_TOP_BOTTOM)
    
    new_im.paste (og, (0, 0,))
    new_im.paste (ud , (0,halfy,))
    new_im.paste (lr , (halfx,0,))
    new_im.paste (lrud , (halfx,halfy,))
    return new_im
    


def loopit (img,iterations,folder)
#!mkdir loop
os.mkdir('loop')
frame_i = 1
for i in xrange(300):
    xpand(img).save("loop/%04d.jpg"%frame_i)
    img = xpand(img)
    frame_i += 1
