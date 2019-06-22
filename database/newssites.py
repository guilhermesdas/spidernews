import pymongo

def getdb(url,name):
    client = pymongo.MongoClient(url)
    db = client[name]
    return db

# add some collection from file
def addcollection(db, colname, dataname):
    # get all collection from file
    pass

# reset
def resetcollection(db,colname):
    db[colname].delete_many({})

# get all frontier links
def getfrontier(db):
    # add all frontier to an list
    frontier = []
    cursor = db["frontier"].find({}).sort("url",-1)
    for doc in cursor:
        frontier.append(doc["url"])
    return frontier

# insert
def addfrontiers(db,links):
    if not(db is None):
        for link in links:
            js = {"url": link}
            if db["frontier"].count_documents(js) == 0:
                db["frontier"].insert_one(js)
    else:
        print("Database error: null object")
