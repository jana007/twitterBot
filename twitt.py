import tweepy

from time import sleep
from config import *

# Access and authorize our Twitter credentials from config.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#tweets a poem provided as a doc, line by line
def tweetPoem():
    #open doc
    file = open('doc.txt', 'rU') #U for universal, \r\n same as \r
    #read lines
    lines = file.readlines()
    #close doc
    file.close()
    
    for line in lines:
        if line != '\n' and line != '\r\n':
            try:
                print(line)
                api.update_status(line)
                sleep(5)
            except:
                print('duplicate status')

#pass the username as paramter
def reTweetStuff(userName):
    #iterate through a specific users tweets, currently limited to 3 pages
    i = 1
    for status in tweepy.Cursor(api.user_timeline, id=userName).items(5):
        # process status here
        #process_status(status)
        print(i)
        i += 1
        api.retweet(status.id)

reTweetStuff('JoshuaAJarrett')
#tweetPoem()


