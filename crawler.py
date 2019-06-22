from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import json
from LinkParser import LinkParser
from database.newssites import *

# parser url, returning html page and list of hyperlinks
def parserURL(baseUrl,url):

    # get html
    htmlBytes = urlopen(url).read()
    htmlString = htmlBytes.decode("utf-8")

    # parser for links
    parser = LinkParser()
    parser.baseUrl = baseUrl
    parser.feed(htmlString)

    return htmlString, parser.links

# parser html, returnig list of founded keywords
def parserHTML(keywords,html):

    foundedkeywords = []

    # search for keywords
    for keyword in keywords:
        if ( html.find(keyword) > -1 ):
            foundedkeywords.append(keyword)

    return foundedkeywords

###########################################################

# database
dburl = "mongodb://localhost:27017/"
dbname = "newssites"
db = getdb(dburl,dbname)

# recursive function
def spider(baseUrl, index, max):

    # current url from frontier
    if ( index < max ):
        url = getfrontier(db,index)
    else:
        return

    # parser one url and add new founded links to database
    html, links = parserURL(baseUrl,url)
    addfrontiers(db,links)
    # see if frontier has changed
    # print("frontier len:",len(getfrontiers(db)))

    # parser one html and add to repository if keyword was founded
    foundedkeywords = parserHTML(getkeywords(db),html)
    if ( len(foundedkeywords) > 0 ):
        js = { "baseurl": baseUrl, "url": url, "keywords": foundedkeywords }
        addrepository(db,js)

    # next url
    index = index + 1
    spider(baseUrl,index,max)

    # see if repository has changed
    # print("repository len: ",len(getrepository(db)))

# run spider
spider("http://portaldoholanda.com.br/",0,10)
#resetcollection(db,"frontier")
#resetcollection(db,"repository")
frontiers = getfrontiers(db)
print(frontiers, len(frontiers))
input()
repository = getrepository(db)
print(repository,len(repository))
input()