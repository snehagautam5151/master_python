import sys, datetime
from pymongo import MongoClient

try:
    client = MongoClient("localhost",27017)
    print("connected to MongoDB")
    db = client.test_databases
    print("db test_database")
    collection = db.test_collection
    print("collection test_collection")
    print("\nGet on documents: " )
    print(collection.find_one())
    print("\nGet all documents: " )
    print(list(collection.find()))
    for x in collection.find():
        print(x)
        print("\nGet only some fields: author and text")
        for x in collection.find({},{"_id":0,"author":1,"text":1}):
            print(x)
            print("\nExclude the author field")
            for x in collection.find({},{"author:0"}):
                print(x)
except:
    e = sys.exc_info()[0]
    print("error: %s" % e)
    
    