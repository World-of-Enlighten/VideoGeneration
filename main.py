from src.scraper import Scraper
from flask import Flask, request

app = Flask(__name__)
scraper = Scraper()
@app.route('/')
def index():
    return "API is alive, check the <a href='https://github.com/World-of-Enlighten/TikTokTrendsAPI/blob/main/README.md'>readme</a> for usage instructions."

@app.route('/api/tiktok/hashtags/', methods=['POST'])
def postTiktokHashtags():
    dat = request.get_json()
    if 'numHashtags' in dat:
        numHashtags = dat['numHashtags']
    else:
        numHashtags = 9
    if 'tag' in dat:
        tag = dat['tag']
    else:
        tag = 'Health'
    return scraper.tiktokHashtags(numHashtags, tag)

@app.route('/tiktok/hashtags/')
def getTiktokHashtags():
    return scraper.tiktokHashtags()


if __name__ == '__main__':
    app.run(debug=True)
