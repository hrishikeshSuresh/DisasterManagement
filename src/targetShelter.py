#!/usr/bin/env python

from pymongo import MongoClient

client = MongoClient('localhost', port = 27018)

#printing all databases
print(client.database_names())

if("SourceDB" in client.database_names()):
	print("Database present\n")

#connecting to database
db = client.SourceDB


