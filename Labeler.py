import os,sys
import re
from writer import writetofile as writer
from writer import downloader as downloader
import writer
dictwriter=writer.writedict()
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

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
                labels=[label.strip() for label in labels]
                print(labels)
            global stop_words
            stop_words=set(stopwords.words("english"))
        
    def classify(self, s):
        #get info of the submission first
        id=str(s.id)
        author=str(s.author)
        name=str(s.name)
        title=str(s.title)
        selftext=str(s.selftext)
        url=str(s.url)
        permalink=str(s.permalink)
        
        urltype=url[-3:]
        if(urltype=='gif' or urltype=='jpg' or urltype=='png'):
            downloader.download(url)
            print('ahhhhhh')
            
        label=self.label(title)
        if(len(label)==0):
            label=['Misc']
        data=[label,[title,name,selftext,url,permalink]]
        print(label)
        return (data)
    
    def label(self,text):
        words=word_tokenize(text)
        words=[word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        print(words)
        print("-------------------------")
        words=self.lemmatize(nltk.pos_tag(words))
        print("wordsdsdfsfa:",words)
        textLabels=[a for a in words if a in labels]
        print("sdafasdfasdf")
        print(textLabels)
        return textLabels
        
    def lemmatize(self, pos):
        print("Lemmatizing")
        print(pos)
        wordlist=[]
        for tuplee in pos:
            type=tuplee[1][:1]
            if type=='R':
                templist=self.lemAdverbs(tuplee[0])
                for a in templist:
                    wordlist.append(a)
            elif type=='V':
                wordlist.append(lem.lemmatize(tuplee[0],'v'))
            else:
                wordlist.append(lem.lemmatize(tuplee[0]))
        dictwriter.addlabels(wordlist)
        return wordlist        
    
    def lemAdverbs(self,word):
        possible_adj = []
        for ss in wn.synsets(word):
            for lemmas in ss.lemmas(): # all possible lemmas
                for ps in lemmas.pertainyms(): # all possible pertainyms
                    possible_adj.append(ps.name())
        return possible_adj
    
    