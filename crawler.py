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

# consts
baseUrl = 'http://portaldoholanda.com.br/'
url = "https://www.portaldoholanda.com.br/noticia-hoje/curso-de-cuidador-de-idoso-tem-pre-inscricoes-abertas-nesta-segunda-feira-em-manaus"
dburl = "mongodb://localhost:27017/"
dbname = "newssites"

# database
db = getdb(dburl,dbname)

# parser one url
html, links = parserURL(baseUrl,url)
# print(links)
addfrontiers(db,links)
# see if frontier has changed
print("frontier len:",len(getfrontier(db)))

# parser one html and add to repository if found keyword
foundedkeywords = parserHTML(getkeywords(db),html)
if ( len(foundedkeywords) > 0 ):
    js = { "baseurl": baseUrl, "url": url, "keywords": foundedkeywords }
    addrepository(db,js)
# see if repository has changed
print("repository len: ",len(getrepository(db)))