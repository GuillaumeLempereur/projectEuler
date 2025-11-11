# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:20:20 2017

@author: lempereu
"""

"""
import Image, ImageDraw

im
s = "Fa"
for i in range(10):
    ns = ""
    for l in s:
        if l == 'a':
            ns += "aRbFR"
        elif l == 'b':
            ns += "LFaLb"
        else:
            ns += l
    s = ns
    print(s)
"""
from PIL import Image, ImageDraw

im = Image.open("lena.pgm")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")