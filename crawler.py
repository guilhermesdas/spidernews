from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import json
from LinkParser import LinkParser

class Crawler:

    def parser(self,url):
        parser = LinkParser()
        response = urlopen(url)
        htmlBytes = response.read()
        # Note that feed() handles Strings well, but not bytes
        # (A change from Python 2.x to Python 3.x)
        htmlString = htmlBytes.decode("utf-8")
        parser.feed(htmlString)
        return htmlString, parser.links

# Class test
crawler = Crawler()
print(crawler.parser("http://portaldoholanda.com.br/"))
