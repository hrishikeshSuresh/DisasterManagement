# -*- coding: utf-8 -*-
"""

@author: Guruprasad
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "925979131631738880-wvSrmzsvKIYY6LzO6zHG8AoUBaxOejI"
access_token_secret = "h8U3nlN6EI3cnkvzP4fGASYGqRsDj9dFrLc7x4ECqWwcQ"
consumer_key = "sH9q4YbFMWa9wdT83RSrXCAds"
consumer_secret = "mGlUo1MY52bceFdX0KL4r8kPgGwBtcEtYzfndaceLWZOTibTBv"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
        #if(status==420):
            #return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()   #l is a variable here.
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['flood','rescue','donate','relief'])   #async=True

