from crawler import *
import threading

##################################### RUN #####################################

def runspider(url):
    initfrontier(db)
    spider(url,0)
    repository = getrepository(db)
    print(repository,len(repository))
    input()


# run spider
resetcollection(db,"frontier")
resetcollection(db,"repository")

runspider("https://www.acritica.com/")

#seeds = getseeds(db)
#for seed in seeds:
#    print(seed)
#    threading._start_new_thread( runspider, [seed] )
# = getfrontiers(db)
#print(frontiers, len(frontiers))
#input()