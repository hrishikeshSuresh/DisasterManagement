#!/usr/bin/env python

from pymongo import MongoClient
import sys

client = MongoClient('localhost', port = 27018)

db = client.SourceDB

target = db.targetCollection
current = db.currentCollection

#connecting to database
db = client.SourceDB

#connecting to collection(table)
target = db.targetInfo

row1 = target.insert_one({"Shelter Name" : "PES University", "Manager Name" : "Jawahar", "Food Packets" : 200, "Sanitary Napkins" : 100, "Water Bottles" : 300, "Medkits" : 10, "Blankets" : 100, "Clothes" : 100, "Location" : "Banashankari"})

current = db.currentInfo

row2 = target.insert_one({"Shelter Name" : "PES University", "Manager Name" : "Jawahar", "Food Packets" : 10, "Sanitary Napkins" : 10, "Water Bottles" : 0, "Medkits" : 1, "Blankets" : 10, "Clothes" : 500, "Location" : "Banashankari"})


client.close()
