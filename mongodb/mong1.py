import pymongo

mcli = pymongo.MongoClient("mongodb://localhost:27017/") #Establish Connection
bkdb = mcli["bank"]
print(mcli.list_database_names())
acc = bkdb["account"]
print("Collection is created")
print(mcli.list_database_names())
