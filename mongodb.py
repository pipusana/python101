import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["web"]
mycol = mydb["weblist"]

result = mycol.find_one({ '_id': 'web_00000144f7f3fa9ae633c5099d013a40_1504700385'})

print(result)