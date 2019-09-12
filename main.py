import nltk,os
import praw
import Labeler

'''nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text=sent_tokenize(text)
print (tokenized_text)'''

#initialize praw to certain subreddit
def startRedditBot(subname):
    reddit=praw.Reddit('bot1',user_agent='Smart Bot')
    global sub
    sub=reddit.subreddit(subname)
    
#adds already read post.ids to file
def addToLogs():
    print("adding read posts to logs")
    with open(log,'w') as f:
        for post_id in posts_collected:
            f.write(post_id+'\n')

def createDirectories():
    if not os.path.exists(HOME):
        print("Creating directories for first time")
        os.mkdir(HOME)
        os.mkdir(DATA)
        os.mkdir(HTML)
    print("Directories Created")
    
    if not os.path.isfile(log):
        global posts_collected
        posts_collected=[]
    else:
        with open(log,'r') as f:
            posts_collected=f.read()
            posts_collected=posts_collected.split('\n')
            posts_collected=list(filter(None,posts_collected))

#Initialize directories for data and the html files
HOME='home/'
DATA='home/data'
HTML='home/html'
log='home/id.txt'

createDirectories()
startRedditBot('all')
labeler=Labeler.Labeler()

for submission in sub.hot(limit=3):
    if(submission not in posts_collected):
        posts_collected.append(submission.id)
        print(submission.title)

addToLogs()
