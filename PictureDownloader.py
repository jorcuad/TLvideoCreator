from TwitterSearch import *
import urllib

try:
	tso = TwitterSearchOrder()
	tso.set_keywords(['#bodas']) #Hashtag a buscar.
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
			urllib.urlretrieve(media[0]['media_url'],"./pics/originals/"+str(i)+".jpg") #TODO catch img format
			i = i+1
		except:
			print 'Tweet sin imagen.'
except TwitterSearchException as e:
	print(e)