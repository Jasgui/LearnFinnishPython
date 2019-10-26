import pymongo

myClient = pymongo.MongoClient("mongodb://178.128.244.93:27017")

mydb = myClient["myDataBase"]

mycol = mydb["Customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x.inserted_id)
