from PIL import Image
import sys
from os import path
from sys import argv

mask = "./frames/"

def main():
	argv = sys.argv
	if len(argv) < 2:
		print 'There is no images to blend.'
		exit(-1)

	files = argv[1:]
	i = 0
	for file in files:
		if path.splitext(file)[1].upper() == '.JPG':
			picture = Image.open(file)
			frame = Image.open(mask+str((i%3)+1)+".png")
			#out = Image.blend(picture, frame, 0.5)
			picture.paste(frame, (0,0), frame)
			picture.save("./pics/blended/"+file.split("/")[3])
			i = i + 1
	exit(0)

if __name__ == '__main__':
	main()