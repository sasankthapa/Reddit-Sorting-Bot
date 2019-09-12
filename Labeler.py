import os,sys
import re

class Labeler:

     def __init__(self):
        if not os.path.isfile('labels.txt'):
            print("Error labels.txt not found... Exiting")
            sys.exit()
        else:
            with open('labels.txt','r') as f:
                global labels
                labels=f.read()
                labels=labels.split(',')
                labels=list(filter(None,labels))
        print(labels)
        
    #def getLabel(self, text):
        