from TwitterSearch import *
import urllib

try:
	tso = TwitterSearchOrder()
	tso.set_keywords(['#HoyTocaHappyHours']) #Hashtag a buscar.
	tso.set_include_entities(True)

	ts = TwitterSearch(
		consumer_key = 'FPNOGw7VTGEJqfaV6BOFF8Bmr',
		consumer_secret = '1Hv4amjuUh1WTgALOwGhizFMx5KYrxQuNd2s5DSKYxH6rdHNY2',
		access_token = '227805236-RNxXUFog9m1s0N2bOMpZQKLduXeO2UnYOu7mVOuW',
		access_token_secret = 'ow74buUsXjBbnU97SHv94CC64Ks39TGq0k9mwFysvrfk3'
	)

	i = 0 #TODO do in apythonic way
	for tweet in ts.search_tweets_iterable(tso):
		try:
			media = tweet['entities']['media']
			print( '%s' % (media[0]['media_url']))
			urllib.urlretrieve(media[0]['media_url'],"./pics/"+str(i)+".jpg") #TODO catch img format
			i = i+1
		except:
			print 'Tweet sin imagen.'
			i = i+1
except TwitterSearchException as e:
	print(e)