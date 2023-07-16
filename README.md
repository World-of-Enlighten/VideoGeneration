# Scraper API

1. <a href="#tiktok-hashtags">Tiktok Hashtags</a>
1. <a href="#ask-gpt">Ask GPT</a>


### Todo list

[x] Get Tiktok trending Hashtags<br>
[] Get TikTok trending songs<br>
[x] Prompt to GPT<br>
[x] Caption generation<br>
[] Default video templates with HTML/CSS<br>
[] Video generation with Deforum
## Tiktok Hashtags

Use : 
```py
scraper = Scraper()
print(scraper.tiktokHashtags())
```

Note that all the variables in this function are optionnals. <br>


- `<number hashtags>` is `9`
- `<your tag>` is `Health`


Replace `<number hashtags` by any positive integer between 3 and 100.
Replace `<your tag>` by one of the tags available in <a href="https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en">TikTok Creative Center</a>.

<details>
<summary>Tags Available</summary>
- Apparel & Accessories<br>
- Baby, Kids & Maternity<br>
- Beauty & Personal Care<br>
- Business Services<br>
- Education<br>
- Financial Services<br>
- Food & Beverage<br>
- Games<br>
- Health<br>
- Home Improvement<br>
- Household Products<br>
- Life Services<br>
- News & Entertainment<br>
- Pets<br>
- Sports & Outdoor<br>
- Tech & Electronics<br>
- Travel<br>
- Vehicle & Transportation<br>
</details>

## Ask GPT

There is two ways to prompt to GPT, the first one uses GPT-4 through <a href="https://you.com">you.com</a> and <a href="https://playwright.dev">playwright.dev</a> the second one 