import sys
import math
from os import path
from sys import argv
from PIL import Image

def isinteger(x):
	try:
		return int(x) == x
	except:
		return False

def tointeger(x):
	try:
		return int(x)
	except:
		return 0

def main():
	argv = sys.argv
	if len(argv) < 2:
		print 'There is no images to resize'
		exit(-1)

	W = 800
	H = 600

	files = argv[1:]
	print files
	for file in files:
		if path.splitext(file)[1].upper() == '.JPG':
			tf = path.splitext(file)
			im = Image.open(file)
			w,h = im.size
			scalex = w/float(W)
			scaley = h/float(H)
			if scalex > scaley:
				scale = scalex
			else:
				scale = scaley
			w = int(w/scale)
			h = int(h/scale)
			im_out = im.resize((w,h), Image.BICUBIC)
			im_out = im_out.convert('RGBA')
			background = Image.new('RGBA', (W,H), (0,0,0,0))
			xi = int(math.fabs(W-w)/2)
			xf = int(math.fabs(W+w)/2)
			yi = int(math.fabs(H-h)/2)
			yf = int(math.fabs(H+h)/2)
			background.paste(im_out,(xi,yi,xf,yf))
			im_out = background
			im_out.save("./pics/resized/"+tf[0].split('/')[3]+'_'+str(W)+'x'+str(H)+tf[1])
	exit(0)

if __name__ == '__main__':
	main()
