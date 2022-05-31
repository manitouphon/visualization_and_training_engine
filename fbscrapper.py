import time
from random import randrange
from facebook_scraper import get_posts
import csv

tmp=[]
def doSleep():
    sleep_time = randrange(30,90)
    print("Sleeping for ",sleep_time, " seconds.")
    time.sleep(sleep_time)



for post in get_posts('phnompenhpost', pages=10):
    print(post['text'])

    #sleep to avoid getting temp banned by FB
    doSleep()
    f = open('PPPostFBScrape.csv','a', encoding='UTF8') #open csv with append moode
    append = csv.writer(f) #make writer var
    tmp=[] #Clear tmp


    post_title = post['post_text']
    likes = post['likes']
    shares = post['shares']
    comments = post['comments']
    print(post_title,'\n' ,likes,'\n',shares,'\n',comments)

    tmp.append(post_title)
    tmp.append(likes)
    tmp.append(shares)
    tmp.append(comments)
    
    append.writerow(tmp) #append csv
    f.close() #close file in case FB ban, result in losing data. 
        