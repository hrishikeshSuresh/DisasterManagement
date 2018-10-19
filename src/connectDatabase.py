#importing MongoClient from PyMongo
from pymongo import MongoClient

#importing pandas and other libraries
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import sys
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
collection1 = db.shelterInfo

#selecting all rows in collection
data_json = collection1.find()
print(data_json)

#creating sql file which can be run into mongodb directly from bash
fp = open("tweets.sql", "w")
fp.write("use SourceDB\n")
fp.write("show collections\n")

#variable to see which lines from input are not recognized
i = 0
#for inserting values into collection
with open("tweets_sample.json") as f:
#for line in sys.stdin:
	for line in f:
		pprint(line)
		try:	
			#row = collection1.insert_one(line)
			fp.write("db.shelterInfo.insert("+ line +")\n")
			#print(row.inserted_id)
		except:
			print(i)
			i = i + 1
			pass;

fp.close()
#or use sys.stdin if data is too large
#can be added depending on the size of json file

data_json = collection1.find()
print(data_json)

#to get description and summary of data
data = pd.DataFrame(list(collection1.find()))

for x in data:
	#whatever computation that has to be done	
	pass;

print(data.describe())
data.plot()

scatter_matrix(data, figsize = (10, 10))
plt.show()
