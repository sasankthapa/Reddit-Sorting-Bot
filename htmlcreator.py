import os
import csv

HTML='home/HTML/'
res='V:/pythonntlk/home/res/'
data='home/data/'

class htmlcreator:

    @classmethod
    def createAll(cls):
        #check if css exist, if not create it.
        if not os.path.isfile(HTML+'stylle.css'):
            cls.createCSS()
        for filename in os.listdir(data):
            print(filename)
            global f
            f=open(HTML+filename.split('.')[0]+'.html','w+',encoding='utf-8')
            cls.startHTML(filename.split('.')[0])
            cls.createEach(filename.split('.')[0].capitalize())
            cls.endHTML()
    
    @classmethod
    def startHTML(cls,title):
        f.write("<html>"+'\n')
        f.write("<head>"+'\n')
        f.write('<link rel="stylesheet" href="stylle.css">'+'\n')
        f.write("<title>"+'\n')
        f.write(str(title)+'\n')
        f.write("</title>"+'\n')
        f.write("</head>"+'\n')
        f.write("<body>"+'\n')      
        f.write('''<div class="header"> \n
                    <h2>'''+str(title)+'''</h2>  \n
                </div>\n''')
       
    @classmethod
    def endHTML(cls):
        f.write('</body>'+'\n')
        f.write('</html>'+'\n')
        f.close()
        
    @classmethod
    def createEach(cls, filename):
        s=open(data+filename.lower()+'.csv',encoding='utf-8')
        reader=csv.reader(s)
        for line in reader:
            f.write('<div class="post">'+'\n')
            f.write('<h1>'+line[0]+'</h1>'+'\n')
            if(line[2]!=""):
                f.write('<p>'+line[2]+ '</p> \n')
            #add button to link to original reddit page
            url=line[3]
            if url[-3:]=='gif' or url[-3:]=='png' or url[-3:]=='jpg':
                filename=url.split('/')
                filename=filename[len(filename)-1]
                cls.addimage(res+filename)
            else:
                print(url)
                f.write('<a href="'+url+'"><button>Url of Post</button></a>')
            
            f.write('<a href="http://www.reddit.com'+line[4]+'"><button>Original</button></a>')
            f.write("</div>"+'\n')
        print('---------------------------------------')
        
    @classmethod
    def addimage(cls, imagename):
        f.write('<a href="'+imagename+'" target="_blank"><img src="'+imagename+'"></a>')
    
    #this method creates the CSS file for the HTML page
    #it only runs once, if you made changes to the css code, delete the .css file from HTML folder then run again
    @classmethod
    def createCSS(cls):
        c=open(HTML+'stylle.css', 'w+')
        c.write('img {float: right;	width:100%; height:100%px; margin-left:15px;}' + '\n')
        c.write('button{margin-left:10px;}'+'\n')
        c.write('p{margin-bottom:10px;}'+'\n')
        c.write('.header{background-color: #f1f1f1;	padding: 10px; text-align:center; margin-bottom:20px;}'+'\n')
        c.write('.post{	background-color: #1f1f1f;	height:190px; padding: 10px; color:white; border-bottom:6px solid red;height:auto;margin-bottom:10px;}'+'\n')
        c.close()