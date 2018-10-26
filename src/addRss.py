#!/usr/bin/env python

#importing MongoClient from PyMongo
from pymongo import MongoClient

#importing pandas and other libraries
import pandas as pd
import matplotlib.pyplot as plt
import pprint
import sys
import json
import ast
from pandas.tools.plotting import scatter_matrix

#creating MongoClient object
client = MongoClient('localhost', port = 27018)

#printing all databases
print(client.database_names())

if("SourceDB" in client.database_names()):
	print("Database present\n")

#connecting to database
db = client.SourceDB

#connecting to collection(table)
collection1 = db.rssInfo

pp = pprint.PrettyPrinter(indent = 2)
#pl = collection1.insert_one({"author":"mike"})


#selecting all rows in collection
data_json = collection1.find()

#print(collection1.find())

#creating sql file which can be run into mongodb directly from bash
fp = open("tweets.sql", "w")

fp.write("use SourceDB\n")
fp.write("show collections\n")

#variable to see which lines from input are not recognized
i = 0
#for inserting values into collection
with open("tweet_src.txt") as f:
#for line in sys.stdin:
	for line in f:
		try:	
			#row = collection1.insert_one(line)
			line = line.replace("False", "false")
			line = line.replace("True", "true")
			line = line.replace("None", "null")
			fp.write("db.shelterInfo.insert("+ line +")\n")
			pp.pprint(line)
			#print(row.inserted_id)
		except:
			print(i)
			i = i + 1
			pass;

fp.close()
#or use sys.stdin if data is too large
#can be added depending on the size of json file

cursor = collection1.find()
client.close()

exit(0)

#to get description and summary of data
data = pd.DataFrame(list(collection1.find()))

for x in data:
	#whatever computation that has to be done	
	pass;

print(data.describe())
data.plot()

scatter_matrix(data, figsize = (10, 10))
plt.show()
