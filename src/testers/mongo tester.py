from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure


client = MongoClient('mongodb://localhost:27017/dev', serverSelectionTimeoutMS=5000)

try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
    print(f'ping success')
except ConnectionFailure:
    print(f'Server not available')
try:
    db = client.database
    collection = db.collection
    for doc in collection.find():
        print(doc['name'])
except ConnectionFailure:
    print(f'Unable to get dbs')
