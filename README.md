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
## TikTok

### TikTok hashtags

Use : 
```py
scraper = Scraper()
print(scraper.tiktokHashtags(numHashtags=14,tag='Education'))
```

Note that all the variables in this function are optionnals so no need to put anything. <br>
Here are the default values in case you don't put anything for the respective options :

- `<numhashtags>` is `9`
- `<tag>` is `Health`


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

### TikTok Songs

*In progress...*
## Ask GPT

There is two ways to prompt to GPT, the first one uses GPT-4 through <a href="https://you.com">you.com</a> and <a href="https://playwright.dev">playwright.dev</a> the second one use GPT-3 through <a href="https://ava-ai-ef611.web.app/">Ava AI API</a>

### GPT-4

In order ot use GPT-4 function, you should give a prompt, the other arguments of the function are optionnal. 
```py
Scraper().askGPT('hello world',option=None,random=0)
```

- `option` : Choose whether you want default instructions or not. Using `None` it will be a « vanilla » GPT-4, else it would be given instructions about the generation : it will generate captions for a TikTok video depending on a long description. <u>The default value of option is `caption`</u>
- `random` : Since those answers are obtained with a scraper, a login is required, setting random to `True` will login to a newly created account, `False` will login into a pedefined email associated with an existing account.
<u>`random` is set to `False` by default.</u> You will not need to change this, except in case you're not getting answers.

### GPT-3

In order to use the GPT-3 api, the arguments are the same than for GPT-4 except the fact that the `random` argument has been deleted.

```py
print(Completion.create("<your prompt",option='caption'))

```