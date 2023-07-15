from src.scraper import Scraper
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "API is alive, check the <a href='https://github.com/World-of-Enlighten/TikTokTrendsAPI/blob/main/README.md'>readme</a> for usage instructions."

if __name__ == '__main__':
    app.run(debug=True)
