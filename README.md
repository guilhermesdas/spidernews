# spidernews
Crawler implementation in python to collect pages from local news sites with keywords about violence and crimes


# Installation steps

- Install mongodb

https://docs.mongodb.com/manual/administration/install-community/

- Install mongopy (I supposed you already have pip and python installed)

pip install mongopy

Depending on the system, you have to enalbe mongopy service.

- In folder database, run:

python initdb.py

- In root folder, run:

python spider.py

# About the code

Database folder has newssites initialization and API to add, get and reset data and collections from database. Available collections:
- keywords: keywords to be searched in pages
- seeds: homepages of news sites
- frontier: links to be explored, increased in each parsed url
- repository: links that contains some keyword in keywords collection

crawler.py is where the magic happens. Have some main functions:
- parserURL return html and a list of links in given url
- parserHTML return founded keywords in a html
- spider is a function that survey recursivelly from a baseurl until a max number of pages. If some pages contains one of the keywords, will be saved in repository database
