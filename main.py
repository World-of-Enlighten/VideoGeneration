from src.scraper import Scraper
from src.gpt import Completion
#scraper=Scraper()

def getCaption():
    return Completion.g4f(prompt='give me an example',option='caption2')

print(getCaption())