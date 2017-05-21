from TwitterSearch import *
import urllib
import sys
import math
from PIL import Image
from moviepy.editor import ImageSequenceClip
from os import listdir
from os.path import isfile, join, splitext

class Project(object):

	def __init__(self, hashtag, number):
		self.path = "./projects/"+hashtag+"/"
		self.number = number
		self.hashtag = hashtag
		

	def download(self):
		try:
			tso = TwitterSearchOrder()
			tso.set_keywords([self.hashtag]) #Hashtag a buscar, es un array.
			tso.set_include_entities(True)

			ts = TwitterSearch(
				consumer_key = '---KEY---',
				consumer_secret = '---KEY---',
				access_token = '---KEY---',
				access_token_secret = '---KEY---'
			)
			i = 0 #TODO do in apythonic way
			for tweet in ts.search_tweets_iterable(tso):
				try:
					media = tweet['entities']['media']
					print( '%s' % (media[0]['media_url']))
					urllib.urlretrieve(media[0]['media_url'],self.path+"originals/"+str(i)+".jpg") #TODO catch img format
					i = i+1
				except:
					print 'Tweet sin imagen.'

				if(i == int(self.number)+1):
					break

		except TwitterSearchException as e:
			print "Download variable initialitation fail."
			print(e)

	# selected : [0 or 1]
	def resize(self, selected):
		W = 800
		H = 600
		#TODO borrar contenido carpeta resized en caso de haberlo
		for i, val in enumerate(selected):
			if val == 1:
				path = self.path+"originals/"+str(i)+".jpg"
				if splitext(file)[1].upper() == '.JPG':
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
					im_out.save(self.path+"/resized/"+tf[0].split('/')[3]+'_'+str(W)+'x'+str(H)+tf[1])

	# toblend : [paths]
	def blend(self):
		#TODO borrar contenido carpeta blend en caso de haberlo
		files = [self.path+"resized/"+f for f in listdir(self.path+"resized") if isfile(join(self.path+"resized",f))]
		i = 0
		for file in files:
			if path.splitext(file)[1].upper() == '.JPG':
				picture = Image.open(file)
				frame = Image.open(mask+str((i%3)+1)+".png")
				#out = Image.blend(picture, frame, 0.5)
				picture.paste(frame, (0,0), frame)
				picture.save(self.path+"blended/"+file.split("/")[3])
				i = i + 1

	def video(self):
		images = [self.path+"blended/"+f for f in listdir(self.path+"blended") if isfile(join(self.path+"blended",f))]
		print images

		clip = ImageSequenceClip(images, fps=1)
		clip.write_videofile(self.path+"video/movie.mp4")
