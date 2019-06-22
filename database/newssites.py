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
def getfrontiers(db):
    # add all frontier to an list
    frontier = []
    cursor = db["frontier"].find({}).sort("url",1)
    for doc in cursor:
        frontier.append(doc["url"])
    return frontier

# get only one frontier
def getfrontier(db,index):
    # add all frontier to an list
    cursor = db["frontier"].find({})
    return cursor[index]["url"]

# get all frontier links
def getkeywords(db):
    # add all frontier to an list
    keywords = []
    cursor = db["keywords"].find({}).sort("keyword",1)
    for doc in cursor:
        keywords.append(doc["keyword"])
    return keywords

# get all repository
def getrepository(db):
    # add all frontier to an list
    repository = []
    cursor = db["repository"].find({}).sort("baseurl",1)
    for doc in cursor:
        repository.append(doc)
    return repository

# insert
def addfrontiers(db,urls):
    if not(db is None):
        for url in urls:
            js = {"url": url}
            if db["frontier"].count_documents(js) == 0:
                db["frontier"].insert_one(js)
    else:
        print("Database error: null object")

# insert links into repository
# jss has baseurl, url, and list of keywords fields
def addrepository(db,js):
    if not(db is None):
        url = { "url": js["url"] }
        if db["repository"].count_documents(url) == 0:
            db["repository"].insert_one(js)
    else:
        print("Database error: null object")