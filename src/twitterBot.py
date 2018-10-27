#!/usr/bin/env python

import tweepy
import time
import random
import sys #for arguments

access_token = "925979131631738880-wvSrmzsvKIYY6LzO6zHG8AoUBaxOejI"
access_token_secret = "h8U3nlN6EI3cnkvzP4fGASYGqRsDj9dFrLc7x4ECqWwcQ"
consumer_key = "sH9q4YbFMWa9wdT83RSrXCAds"
consumer_secret = "mGlUo1MY52bceFdX0KL4r8kPgGwBtcEtYzfndaceLWZOTibTBv"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

name = sys.argv[1]
shelter_name = sys.argv[2]
location = sys.argv[3]

tweet = "Thank you @"+name+". Please send the promised resources to "+shelter_name+","+location+".#SkelligeTsunamiNotReal"
api.update_status(status = tweet)
print(tweet)
