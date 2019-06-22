import pymongo

def getdb(url,name):
    client = pymongo.MongoClient(url)
    db = client[name]
    return db

# get all frontier links
def getfrontier(db):
    # add all frontier to an list
    frontier = []
    cursor = db["frontier"].find({})
    for doc in cursor:
        frontier.append(doc["url"])
    return frontier