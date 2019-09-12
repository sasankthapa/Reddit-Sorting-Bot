import os,sys
import re

class Labeler:

    def __init__(self): #Get Labels from labels.txt while initializing
        if not os.path.isfile('labels.txt'):
            print("Error labels.txt not found... Exiting")
            sys.exit()
        else:
            with open('labels.txt','r') as f:
                global labels
                labels=f.read()
                labels=labels.split(',')
                labels=list(filter(None,labels))
        
    def label(self, s):
        #get info of the submission first
        id=str(s.id)
        author=str(s.author)
        name=str(s.name)
        title=str(s.title)
        selftext=str(s.selftext)
        url=str(s.url)
        
        f=open("thinking.txt",'w+')
        f.write(id+'\n')
        f.write(author+'\n')
        f.write(name+'\n')
        f.write(title+'\n')
        f.write(selftext+'\n')
        f.write(url+'\n')

        print(vars(s))
        return ("haha"+name)