import nltk,os
import praw
import Labeler
from writer import writetofile as writer
from writer import writedict as dictwriter

#Initialize directories for data and the html files
HOME='home/'
DATA='home/data'
HTML='home/html'
log='home/id.txt'
res='home/res'

'''nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

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
        os.mkdir(res)
       
    if not os.path.isfile(log):
        global posts_collected
        posts_collected=[]
    else:
        with open(log,'r') as f:
            posts_collected=f.read()
            posts_collected=posts_collected.split('\n')
            posts_collected=list(filter(None,posts_collected))

createDirectories()
startRedditBot('Unity3D')
labeler=Labeler.Labeler()

data=[]
for submission in sub.hot(limit=10):
    if(submission  not in posts_collected):
        posts_collected.append(submission.id)
        data.append(labeler.classify(submission))

print(data)

for info in data:
    for i in info[0]:
        print(i)
        writer.write(i,list(info[1]))        
dictwriter.close()

addToLogs()
