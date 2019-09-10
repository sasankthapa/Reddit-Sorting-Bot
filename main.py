import nltk,os
import praw
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text=sent_tokenize(text)
print (tokenized_text)
print
def startRedditBot(subname):
    reddit=praw.Reddit('bot1',user_agent='Smart Bot')
    global sub
    sub=reddit.subreddit(subname)
    
    
def addToLogs():
    print("adding read posts to logs")
    with open(log,'w') as f:
        for post_id in posts_collected:
            f.write(post_id+'\n')
    


def createDirectories():
    if not os.path.exists(HOME):
        print("Creating directories")
        os.mkdir(HOME)
        os.mkdir(DATA)
        os.mkdir(HTML)
        
    if not os.path.isfile(log):
        global posts_collected
        posts_collected=[]
    else:
        with open(log,'r') as f:
            posts_collected=f.read()
            posts_collected=posts_collected.split('\n')
            posts_collected=list(filter(None,posts_collected))
    
    

HOME='home/'
DATA='home/data'
HTML='home/html'
log='home/id.txt'

createDirectories()
startRedditBot('all')

for submission in sub.hot(limit=3):
    if(submission not in posts_collected):
        posts_collected.append(submission.id)
        print(submission.title)

addToLogs()
