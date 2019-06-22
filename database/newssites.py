import pymongo

def getdb(url,name):
    client = pymongo.MongoClient(url)
    db = client[name]
    return db