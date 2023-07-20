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


'''
print(getCaption())

output : 
Join us for a healing afternoon of conscious breathwork and crystal singing bowls in Cambridge. Experience a deep sense of relaxation, let go of what no longer serves you, and find balance. Conscious connected breathwork has many proven benefits for physical and psychological health. Crystal Singing Bowls produce healing frequencies that activate your parasympathetic nervous system, reducing stress and anxiety. Bring warm clothing, water, and a yoga mat. Leave feeling restored, rebalanced, and full of vitality. Contact us for any queries.
'''