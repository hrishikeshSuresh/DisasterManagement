#!/usr/bin/env python

import tweepy
import csv
import pandas as pd
import json
import pprint
import nltk

stops = [',','for','and','.','or']
units = ['liters','liter','kg','L','ML','ml','g','l','pieces', 'units','packets','bottles','packet','bottle','piece','litre','litres']

def Keyvaluesplit (Tweet):
    words = nltk.word_tokenize (Tweet)
    final_list = []
    for i in range(len(words)):
        if (words[i].isnumeric()==True):
            j = i
            temp_list = []
            while (words[j] not in stops):
                if (words[j]!='of'):
                    temp_list.append(words[j])
                j+=1
            final_list.append(temp_list)
    return (final_list)


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

for tweet in tweepy.Cursor(api.search,q="##SkelligeTsunamiNotReal",
                                         lang="en",
                           since="2018-01-01").items():
    #pp.pprint(tweet._json)
	#csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #csvWriter.writerow(str(tweet))
    #f.write(str(tweet._json))
    #f_text.write(str(tweet.text + "^&*"))
    Tweet = str(tweet.text)
    Dic_tweet = tweet._json
    Dic_tweet['Food Packets'] = 0
    Dic_tweet['Sanitary Napkins'] = 0
    Dic_tweet['Water'] = 0
    Dic_tweet['Medkits'] = 0
    Dic_tweet['Blankets'] = 0
    Dic_tweet['Clothes'] = 0
    Final_list = []
    Super_tweet = []
    #Tweet var
    Dict = dict()
    #Final_list.append(Keyvaluesplit(tweet))
    Temp_list = Keyvaluesplit(Tweet)
    #print (Temp_list)
    for L1 in Temp_list:
        for word in L1:
            if word in units:
                L1.remove(word)
    for L1 in Temp_list:
        L1[1] = ' '.join(L1[1:len(L1)])
    for L1 in Temp_list:
        L1 = L1[0:2]
        L1[0],L1[1] = L1[1],L1[0]
        key = L1[0]
        val = int(L1[1])
        Dic_tweet[key] = val
        Dict[key] = val
    #print(type(tweet._json))
    #print (tweet._json + Dict)
    print (Dict)
    print (Dic_tweet)
    f.write(str(Dic_tweet))
    #print (type(tweet))
    #print (type(tweet._json))
    
f.close()
