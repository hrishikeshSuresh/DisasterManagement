#!/usr/bin/env python

from pymongo import MongoClient
import json
from subprocess import call

def checkRSS(target_i, current_j, rssName, db):
	if(target_i[rssName] <= current_j[rssName]): #targets met
		print("Shelter requirements satisfied :", rssName)
		return;
	print(target_i[rssName], current_j[rssName])
	diff = target_i[rssName] - current_j[rssName]
	#search resource
	rssColl = db.rssInfo
	rss_cursor = rssColl.find().sort(rssName, -1)
	#print(list(rss_cursor)[0])
	#if(rss_cursor[rssName] == 0):
	#	print("No spare resources available")
	#	return;
	for i in rss_cursor:
		if(i[rssName] == 0):
			print("No spare resources available")
			return;
		if(diff >= 0):
			if(i[rssName]>0):
				diff-= i[rssName]
				allocated = 0
				if diff<0:
					allocated = diff
					i[rssName] -= diff
				else:
					allocated = i[rssName]
					i[rssName] = 0
				#Tweet
				command = ["python3","twitterBot.py",i["user"]["screen_name"],current_j["Shelter Name"],current_j["Location"]]
				print(command)	
				call(command)
				print("Resource %s allocated by %s in amount %d"%(rssName, i["user"]["screen_name"], allocated))
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

rssList = ['Food Packets', 'Sanitary Napkins', 'Water Bottles', 'Medkits', 'Blankets', 'Clothes']

for i in cursor_target:
	for j in cursor_current:
		if(i['Shelter Name'] >= j['Shelter Name']):
			for k in rssList:
				checkRSS(i, j, k, db)
