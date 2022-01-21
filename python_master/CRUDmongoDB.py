import os, sys, datetime
from sys import platform
from pymongo import MongoClient
if platform == "linux":
    os.system('clear')
elif platform == "win32":
    os.system('cls')
try:
    client = MongoClient('localhost',27017)
    print("Connected to MongoDB database") 
    db = client.db_shami
    print("\ncreated db db_shami")
    collection = db.test_collection
    print("\nCreated the Collection test_collection")
    doc = {"author":"shami","text": "My first blog post!","tags" : ["mongodb", "python", "pymongo"],"date":datetime.datetime.utcnow()}
    print("\nCreated the document object")
    doc_id = collection.insert_one(doc)
    print("\nDocument ID :", doc_id.inserted_id)
except:
    e= sys.exe_info()[0]
    print("error:%s" %e)
          