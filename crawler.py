from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import time
import json

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
class LinkParser(HTMLParser):

    links = []
    baseUrl = ''

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                   # if (newUrl.find(self.baseUrl) > -1 ): # And add it to our colection of links:
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        response = urlopen(url)
        htmlBytes = response.read()
        # Note that feed() handles Strings well, but not bytes
        # (A change from Python 2.x to Python 3.x)
        htmlString = htmlBytes.decode("utf-8")
        self.feed(htmlString)
        return htmlString, self.links
    
# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
def spider(url, maxPages):

    frontier = [url]
    index = 0
    parser = LinkParser()
    pages = {}
    pages['link'] = []
    keywords = [ 
        'morte', 'morto', 'morre', 'acidente','assalto', 'hospital', 'medicamento'
    ]

    while( index < maxPages and index < len(frontier) ):
        #print(index,'Current page->',frontier[index])
        data, links = parser.getLinks(frontier[index])
        frontier = list(set(frontier + links))
        #print('new frontier size:',len(frontier))
        index = index + 1
        founded_words = []
        for keyword in keywords:
            if ( data.find(keyword) > -1 ):
                #print(keyword,' founded!')
                founded_words.append(keyword)
        if ( len(founded_words) > 0 ):
            page = {'url':frontier[index],'keywords':founded_words}
            pages['link'].append(page)
            #print(founded_words,frontier[index])
        #print()

    #print(frontier[:maxPages])
    print(json.dumps(pages, indent=4))

# execution
i = 10
while (i > 0):
    spider("https://www.portaldoholanda.com.br/amazonas",10)
    #spider("https://d24am.com/amazonas/",10)
    #spider("https://www.acritica.com/channels/manaus",10)
    i = i - 1