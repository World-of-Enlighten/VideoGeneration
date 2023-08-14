# Video generation

In order to have distinguishables videos in style while having an harmony in our posts, videos will be respecting norms :
The video template is available in another repo temporarily (<a href="https://github.com/World-of-Enlighten/VideoTemplate">VideoTemplate</a>), during the process it should be in the same directory.
```
#go to the desired folder
git clone https://github.com/World-of-Enlighten/VideoGeneration
cd VideoGeneration
git clone https://github.com/World-of-Enlighten/VideoTemplate
```

- `Intro ~5sec` : *date, title, watermarks, theme / categorie...* 
- `Content` : *Components variables, time variable*
- `Outro ~3sec` : *same components for each videos, with same pos but color scheme may vary*, 


# Builtin functions

<ul>
<li>Video</li>
<ul><a href="#delay">Delay tag</a></ul>
<ul><a href="#branding">Branding tag</a></ul>
<ul><a href="#calendar">Calendar tag</a></ul>
<li>Scrapers</li>
<ul>
<li><a href="#tiktok">Tiktok</a>
<ul><li>Trending hashtags</li><li>Trending songs</li></ul></li>
<li><a href="#ask-gpt">Ask GPT</a>
<ul><li>GPT-4</li><li>GPT-3</li></ul>
</li>
</ul>
</ul>


### Todo list

- [x] Get Tiktok trending Hashtags 
- [x] Get TikTok trending songs 
- [x] Prompt to GPT 
- [x] Caption generation 
- [ ] Default video templates with <a href="https://www.remotion.dev/">remotion</a>
- [ ] Video generation with Deforum
- [ ] Scrap TikTok Creative Assistant
## TikTok

### TikTok hashtags

Use : 
```py
#assuming that you are running in parent dir
from src.scraper import Scraper
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

This function allows you to get all the **approved for business use** songs in TikTok Creative in a list of file url.


```py
#assuming that you are running in parent dir
from src.scraper import Scraper
scraper = Scraper()
print(scraper.tiktokSongs())
```

### TikTok video that uses a song

This function allows you to get the url of a video using the respective song.
```py
#assuming that you are running in parent dir
from src.scraper import Scraper
scraper = Scraper()
print(scraper.tiktokSongsVideoUrl())
```


## Ask GPT

There is two ways to prompt to GPT, the first one uses GPT-4 through <a href="https://you.com">you.com</a> and <a href="https://playwright.dev">playwright.dev</a> the second one use GPT-3 through <a href="https://ava-ai-ef611.web.app/">Ava AI API</a>

### GPT-4

In order ot use GPT-4 function, you should give a prompt, the other arguments of the function are optionnal. 
```py
#assuming that you are running in parent dir
from src.scraper import Scraper
Scraper().askGPT('hello world',option='caption',random=0))
```

- `option` : Choose whether you want default instructions or not. Using `None` it will be a « vanilla » GPT-4, else it would be given instructions about the generation : it will generate captions for a TikTok video depending on a long description. <u>The default value of option is `caption`</u>
- `random` : Since those answers are obtained with a scraper, a login is required, setting random to `True` will login to a newly created account, `False` will login into a pedefined email associated with an existing account.
<u>`random` is set to `False` by default.</u> You will not need to change this, except in case you're not getting answers.

### GPT-3

In order to use the GPT-3 api, the arguments are the same than for GPT-4 except the fact that the `random` argument has been deleted.

```py
#assuming that you are running in parent dir
from src.gpt import Completion
print(Completion.create("hello world",option='caption'))
```

Same for GPT-4, default value of option is `caption` and it is an optional argument.

## <a id="delay">The delay tag</a>

> The delay tag serve for a lot of things. It was meant to make the video generation easier. This component is in charge of :

- Wait time before display
- Fade, with custom frames
- Time of display (choose whether you want to remove the element after a certain time or keep it)
- Typing effect for text


### Wait time
About the delay, wait time is relative to the `Delay` parents. Example below
```tsx
<Delay wait={5}>
Hello world!
<Delay wait={10}>
Foo bar
</Delay>
World hello ?
</Delay>
```
This example will display `Hello world` and `World hello ?` after 5 seconds since they are inside of the `Delay` component. Additionnaly, depending on the position time can be relative. This explains why `Foo bar` will not show at the 10th second but the 15th.

### Fade

You can make an element fading when displaying, this can be done with the following :
```tsx
<Delay fade={20}>
Lorem Ipsum
</Delay>
```
This will lead to a fade of 20 frames. 

### Remove after

If you want to remove elements after a certain amount of time you can use the following :
```tsx
<Delay removeafter={5}>
Bonjour!
</Delay>
```
The following element will disappear after 5 seconds. If you are using `wait` in the same time, it will start counting only after the display of the element so it will still remain visible on screen for 5 seconds. 


### Typing effect

To make a typing effect, you will need to put the text as an argument. Then you can set the typing speed. `typingSpeed` $> 1$ results to a speed up, `typingSpeed` $< 1$ results to speed lowering.
The text will appear at the beggining, so you can still put other elements within the `Delay` tags, they just wont have the typing effect.

```tsx
<Delay text={"Hello world!"} typingSpeed={1}>
```

## <a id="branding">`Branding` tag</a>

This tag allows you to display any branding element given options.
There is two arguments :<br>
- `type` : Type of the branding element<br>
- `theme` : Color scheme of the branding element (by default main green).

## <a id="calendar">`Calendar` tag</a>
![Alt text](image.png)<br>
This tag produces the calendar above. By default it will take the actual date (month and day) but you can change separately the month and the day as you want with the optional arguments of the same name.
