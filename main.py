from src.scraper import Scraper
from src.gpt import Completion
scraper=Scraper()

def getCaption():
    with open("example.txt") as f:
        content=f.read()
    #method 1
    #return Completion.create(content)
    #method 2
    return scraper.askGPT(content)

def sendToRemotion(txt):
    with open("video/src/TextComposition.tsx") as f:
        content=f.readlines()
        content[7]=txt
    with open("video/src/TextComposition.tsx",'w') as f:
        f.write(''.join(content))
    return 1



'''
#this function generate captions and add them to the video
def generateVideo():
    sendToRemotion(getCaption()) #send captions to TextComposition.tsx
'''

