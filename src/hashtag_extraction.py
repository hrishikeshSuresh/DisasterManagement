#!/usr/bin/env python

import tweepy
import csv
import pandas as pd
import json
import pprint

#input your credentials here

access_token = "925979131631738880-wvSrmzsvKIYY6LzO6zHG8AoUBaxOejI"
access_token_secret = "h8U3nlN6EI3cnkvzP4fGASYGqRsDj9dFrLc7x4ECqWwcQ"
consumer_key = "sH9q4YbFMWa9wdT83RSrXCAds"
consumer_secret = "mGlUo1MY52bceFdX0KL4r8kPgGwBtcEtYzfndaceLWZOTibTBv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
#csvFile = open('tweet_dataX.csv', 'w')
f = open('tweet_src.txt', 'w')
f_text = open('tweet_text.txt', 'w')
pp = pprint.PrettyPrinter(indent = 2)
#Use csv Writer
#csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#SkelligeTsunamiNotReal",
                           lang="en",
                           since="2018-10-03").items():
    pp.pprint(tweet._json)
	#csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #csvWriter.writerow(str(tweet))
    f.write(str(tweet._json)+"\n")
    f_text.write(str(tweet.text))
f.close()
