#importing MongoClient from PyMongo
from pymongo import MongoClient

#importing pandas and other libraries
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
from pandas.tools.plotting import scatter_matrix

#creating MongoClient object
client = MongoClient('localhost',port = 27017)

#printing all databases
print(client.list_database_names())

if("SourceDB" in client.list_database_names()):
	print("Database present\n")

#connecting to database
db = client.SourceDB

#connecting to collection(table)
collection1 = db.shelterInfo

#selecting all rows in collection
line = collection1.find()

#for inserting values into collection
with open("mined_data.json") as f:
	for line in f:
		pprint(line)
		row = collection1.insert_one(line)
		print(row.inserted_id)

#or use sys.stdin if data is too large
#can be added depending on the size of json file

for x in line:
	#whatever computation that has to be done	

#to get description and summary of data
data = pd.DataFrame(list(collection1.find()))
print(data.describe())
data.plot()

scatter_matrix(data, figsize = (10, 10))
plt.show()
