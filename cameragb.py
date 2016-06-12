#!/usr/bin/python
# -*- coding: utf-8 -*-
# info: http://pillow.readthedocs.org/en/latest/reference/ImageOps.html
# 		http://www.pixfans.com/game-boy-camera-el-mejor-periferico-de-la-historia/
import sys
from PIL import Image
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw 

size=[128,112,43,1,126,15] #Original size from Camera GameBoy

def fontear(input,output):
	img = Image.open(input)
	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	# source: http://www.fontspace.com/629fonts/nintender
	font = ImageFont.truetype("Nintender.ttf", 14)
	font2 = ImageFont.truetype("Arial Narrow Bold Italic.ttf", 15)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((size[2], size[3]),"Nintendo",(255,255,255),font=font)
#	draw.text((43, 1),"Nintendo",(255,255,255),font=font)
	draw.text((size[2], size[4]),"GAME BOY",(255,255,255),font=font2)
	img.save(output)

def convertir(input,output):
	img2 = Image.open(input)
	resized = ImageOps.fit(img2, (size[0], size[1]), method=Image.ANTIALIAS, bleed=0.05)
	expanded = ImageOps.expand(resized, border=size[5], fill=0).save('temp.JPG')
	fontear('temp.JPG','temp.JPG')
	img3 = Image.open('temp.JPG')
	gray = ImageOps.grayscale(img3)
	posterized = ImageOps.posterize(gray, 3) # (1-8) value 3 is more similar than game boy camera
	posterized.save(output)

#file_input = sys.argv[1]
try:
	file_input = sys.argv[1]
except:
	print "\nErro: A picture file must be defined. For example: IMG001.JPG\n"
else:
	convertir(file_input,"GAMEBOYER.jpg")

