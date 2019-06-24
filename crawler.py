from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import json
import requests
from LinkParser import LinkParser
from database.newssites import *

###########################################################

# database
dburl = "mongodb://localhost:27017/"
dbname = "newssites"
db = getdb(dburl,dbname)

################ FUNCTIONS #################


############ PARSERS ###############

# parser url, returning html page and list of hyperlinks
def parserURL(baseUrl,url):

    # get html
    header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=header)
    htmlString =  r.text
    
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

############ SPIDER ###############

# recursive function to parse html
def spider(baseUrl, index):

    # current url from frontier
    url = getfrontier(db,index)
    if url is None:
        return

    # parser one url and add new founded links to database
    html, links = parserURL(baseUrl,url)
    addfrontiers(db,links)
    # see if frontier has changed
    # print("frontier len:",len(getfrontiers(db)))

    # parser one html and add to repository if keyword was founded
    foundedkeywords = parserHTML(getkeywords(db),html)
    if ( len(foundedkeywords) > 0 ):
        addrepository(db,baseUrl,url,foundedkeywords)

    # next url
    index = index + 1
    spider(baseUrl,index)

    # see if repository has changed
    #repository = getrepository(db)
    #print("Repository:",repository,len(repository))