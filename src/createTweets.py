#!/usr/bin/env python

import tweepy
import time
import random

access_token = "925979131631738880-wvSrmzsvKIYY6LzO6zHG8AoUBaxOejI"
access_token_secret = "h8U3nlN6EI3cnkvzP4fGASYGqRsDj9dFrLc7x4ECqWwcQ"
consumer_key = "sH9q4YbFMWa9wdT83RSrXCAds"
consumer_secret = "mGlUo1MY52bceFdX0KL4r8kPgGwBtcEtYzfndaceLWZOTibTBv"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

user = api.me()
print(user.screen_name)
  
rssList = ['Food Packets', 'Sanitary Napkins', 'Water Bottles', 'Medkits', 'Blankets', 'Clothes']

for i in range(10):
	# update the status 
	tweet = u"We can donate "+str(random.randrange(50,200))+" "+rssList[random.randrange(0,len(rssList), 1)]+", "+str(random.randrange(50,200))+" "+rssList[random.randrange(0,len(rssList), 1)]+" "  +"#SkelligeTsunamiNotReal"
	print(tweet)
	api.update_status(status = tweet)
	time.sleep(60)
