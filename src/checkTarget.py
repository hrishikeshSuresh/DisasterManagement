#!/usr/bin/env python

from pymongo import MongoClient
import sys

client = MongoClient('localhost', port = 27018)

db = client.SourceDB

target = db.targetCollection
current = db.currentCollection

  
