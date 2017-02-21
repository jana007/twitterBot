import tweepy

from time import sleep
from config import *

# Access and authorize our Twitter credentials from config.py
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)




#open doc
file = open('doc.txt', 'rU') #U for universal, \r\n same as \r
#read lines
lines = file.readlines()
#close doc
file.close()
def tweet():
    for line in lines:
        if line != '\n' and line != '\r\n':
            try:
                print(line)
                api.update_status(line)
                sleep(5)
            except:
                print('duplicate status')
                
            
tweet()


