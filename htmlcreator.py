import os

HOME='home/HTML'
res='home/res'
data='home/data'

class htmlcreator:

    @classmethod
    def createAll(cls):
        for filename in os.listdir(data):
            print(filename)
        
    @classmethod
    def createEach(cls, filename):
        f=open(filename,'r',encoding='utf-8')
        f=f.readlines()
        for line in lines:
            line=line.strip(',')
            