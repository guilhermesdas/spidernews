# spidernews
Crawler implementation in python to collect pages from local news sites with keywords about violence and crimes


# 1. Install Mongodb
https://docs.mongodb.com/manual/administration/install-community/

# 2. Install mongopy (I supposed you already have pip and python installed)

pip install mongopy

Depending on the system, you have to enalbe mongopy service.

# 3. In folder database, run:

python initdb.py

# 4. In root folder, run:

python spider.py
