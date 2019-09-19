import csv
import os
import requests
import json

DATA='home/data/'
res='home/res/'
resfile='home/res/log.txt'
dictionary='home/dict.json'

class writetofile:
	
    @classmethod
    def write(cls, filename,data):
        filename=DATA+filename+'.csv'
        if os.path.isfile(filename):
            f=open(filename,'a',encoding='utf-8',newline='')
            writer=csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerows([data])
        else:
            f=open(filename,'w+',encoding='utf-8',newline='')
            writer=csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerows([data])
        f.close()
            

class writedict:
    def __init__(self):
        global f
        global dict
        if os.path.isfile(dictionary):
            f=open(dictionary)
            dict=json.load(f)
        else:
            dict={}
        
    def addlabels(self,labels):
        for i in labels:
            print(type(dict))
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
    
    @classmethod
    def close(cls):
        with open(dictionary,'w+') as f:
            json.dump(dict,f)
        f.close()
        
class downloader:
               
    @classmethod
    def download(cls, url):
        filename=url.split('/')
        filename=filename[len(filename)-1]
        r=requests.get(url)
        with open(res+filename,'wb') as f:
            f.write(r.content)
        f.close()