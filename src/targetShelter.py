#!/usr/bin/env python

from pymongo import MongoClient
import json

def checkRSS(target_i, current_j, rssName, db):
	if(target_i[rssName] <= current_j[rssName]): #targets met
		print("Shelter requirements satisfied :", rssName)
		return;
	print(target_i[rssName], current_j[rssName])
	diff = target_i[rssName] - current_j[rssName]
	#search resource
	rssColl = db.rssInfo
	rss_cursor = rssColl.find().sort(rssName, -1)
	if(rss_cursor[0][rssName] == 0):
		print("No spare resources available")
		return;
	for i in rss_cursor:
		if(diff >= 0):
			if(i[rssName]>0):
				diff-= i[rssName]
				allocated = 0
				if diff<0:
					allocated = diff
				else:
					allocated = i[rssName]
				#Tweet
				print("Resource {} allocated by {} in amount {}"%(rssName, i[screen_name], allocated)
				i[rssName]-=allocated
				current_j[rssName]+=allocated
	return;

client = MongoClient('localhost', port = 27017)

#printing all databases
print(client.database_names())

if("SourceDB" in client.database_names()):
	print("Database present\n")

#connecting to database
db = client.SourceDB

target = db.targetInfo
current = db.currentInfo

cursor_target = target.find()
cursor_current = current.find()

rssList = ['Food Packets', 'Sanitary Napkins', 'Water', 'Medkits', 'Blankets', 'Clothes']

for i in cursor_target:
	for j in cursor_current:
		if(i['Shelter Name'] >= j['Shelter Name']):
			for k in rssList:
				checkRSS(i, j, k, db)
