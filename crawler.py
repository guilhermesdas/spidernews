from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import json
from LinkParser import LinkParser
from database.newssites import getdb

# parser url, returning html page and list of hyperlinks
def parser(url,baseUrl):
    parser = LinkParser()
    response = urlopen(url)
    htmlBytes = response.read()
    # Note that feed() handles Strings well, but not bytes
    # (A change from Python 2.x to Python 3.x)
    htmlString = htmlBytes.decode("utf-8")
    parser.baseUrl = baseUrl
    parser.feed(htmlString)
    return htmlString, parser.links

# insert
def addfrontiers(db,links):
    if not(db is None):
        for link in links:
            js = {"link": link}
            if not((db)["frontier"].find(js)):
                db["frontier"].insert_one(js)

###########################################################

# consts
baseUrl = 'http://portaldoholanda.com.br/'
dburl = "mongodb://localhost:27017/"
dbname = "newssites"

# database
db = getdb(dburl,dbname)

# parser one html
html, links = parser(baseUrl,baseUrl)
print(html)
print(links)