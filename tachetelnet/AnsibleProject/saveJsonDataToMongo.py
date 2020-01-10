import json
import pymongo
import sys
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test']
collection_currency = db['currency']
#collection_currency.drop()
with open(sys.argv[1]) as f:
    file_data = json.load(f)


# use collection_currency.insert(file_data) if pymongo version < 3.0
collection_currency.insert(file_data)
client.close() 
 

