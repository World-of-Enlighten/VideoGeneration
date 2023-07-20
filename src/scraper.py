from playwright.sync_api import Playwright, sync_playwright

try:
    from src.util.functions import *
    import src.util.data as data
    from src.util.mail import *
except:
    from util.functions import *
    import util.data as data
    from util.mail import *

class Scraper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.webkit.launch(headless=True)
        self.context = self.browser.new_context(
            geolocation={"longitude": -0.293679, "latitude": 51.453212},
            permissions=["geolocation"],
            locale='en-GB',
            timezone_id='Europe/London',
        )
        self.page = self.context.new_page()

    def teardown(self):
        self.context.close()
        self.browser.close()

    def tiktokHashtags(self,numHashtags=9,tag='Health'):
        if tag not in data.tiktokTags:
            raise AssertionError("Error, your tag does not exist. The tag should be one of the tags available in TikTok creative, ")
        if type(numHashtags)!=int or numHashtags<3 or numHashtags>100:
            raise AssertionError("Error, the numHashtags value is incorrect. It should be an integer comprised between 3 and 100.")
        else:
            numHashtags=roundToMultiple(numHashtags)
        self.page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en")

        # [1] Change region
        self.page.click('span[data-testid="cc_rimless_select_undefined"]')
        print("[1] Region changed")

        # [2] Set to UK
        self.page.get_by_placeholder("Start typing or select from the list").click()
        self.page.get_by_placeholder("Start typing or select from the list").fill("united kin")
        self.page.get_by_test_id("cc_rimless_select_undefined_item_68").click()
        print("[2] Set to UK")

        # [3] Change hashtags
        self.page.locator("#hashtagIndustrySelect").get_by_role("img").click()
        self.page.get_by_test_id("cc_single_select_undefined_item_8").get_by_text(tag).click()
        print(f"[3] Tag set to {tag}")

        # [4] View more hashtags
        for i in range(numHashtags):
            self.page.get_by_test_id("cc_contentArea_viewmore_btn").get_by_text("View More").click()
            print(f"[3.{i}] Clicked view more button")
        print("[4] End click view more button")

        # [5] Getting hashtags
        health_hashtags = self.page.query_selector_all('.CardPc_titleText__RYOWo')
        output = []
        print("[5] Got hashtags")
        for hashtag in health_hashtags:
            output.append(hashtag.inner_text()[2:])
        self.teardown()
        return output

    def googleMaps(self,timeout=10000):
        #this function allows to check geolocation settings
        #you should click on button "Your location", otherwise it'll be your real location
        #disable headless
        self.page.goto("https://maps.google.com")
        self.page.wait_for_timeout(timeout)
        self.teardown()

    def browserOpen(self):
        self.page.goto("https://google.com")
        while True:
            pass

    def askGPT(self,prompt,random=0, option='caption'):
        self.page.goto("https://you.com")
        self.page.screenshot(path="screenshot.png")
        self.page.locator("body").click()
        self.page.get_by_test_id("sign-in-button").click()
        self.page.get_by_placeholder("example@email.com").click()
        if random:
            mailbox=getRandomMailbox()
            self.page.get_by_placeholder("example@email.com").fill(mailbox)
            self.page.get_by_role("button", name="Continue with email").click()
            self.page.get_by_role("textbox", name="Password").click()
            self.page.get_by_role("textbox", name="Password").fill("thisismypassword&")
            self.page.get_by_role("button", name="Continue").click()
        else:
            mailbox=getEnlightenMailbox()
            self.page.get_by_placeholder("example@email.com").fill(mailbox)
            self.page.get_by_role("button", name="Continue with email").click()
            while True:
                try:
                    self.page.goto(getLoginLink(mailbox))
                    break
                except:
                    pass
        self.page.get_by_test_id("search-input").click()
        self.page.get_by_test_id("search-input").fill(data.prompts[option])
        self.page.get_by_test_id("submit-button").click()
        answer = self.page.query_selector_all("p[data-testid=youchat-text]")
        #print(answer[0].inner_text())
        self.page.get_by_test_id("youchat-input-textarea").click()
        self.page.get_by_test_id("youchat-input-textarea").fill(prompt)
        self.page.get_by_test_id("youchat-input").get_by_role("button").click()
        self.page.wait_for_timeout(3000)
        #final_answer=self.page.query_selector_all("p[data-testid=youchat-text]")
        final_answer=re.findall('''<p data-testid="youchat-text"(.*?)</p>''',self.page.content())
        while "Stop generating" in self.page.content():
            #print("[P] Generation in progress")
            final_answer=re.findall('''<p data-testid="youchat-text"(.*?)</p>''',self.page.content())
        self.teardown()
        out=[]
        for ans in final_answer:
            out.append(''.join(ans.split('">')[1:]))
        return out[1]
    
    def tiktokSongs(self,numSongs=10):

        #Determine how many times you need to click on view more
        getSongs=numSongs
        numSongs-=3
        numSongs//=3
        if numSongs%3!=0:
            numSongs+=1

        #Open the page
        self.page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/music/pc/en")


        # [1] Change region
        self.page.click('span[data-testid="cc_rimless_select_undefined"]')
        print("[1] Region changed")

        # [2] Set to UK
        self.page.get_by_placeholder("Start typing or select from the list").click()
        self.page.get_by_placeholder("Start typing or select from the list").fill("united kin")
        self.page.get_by_test_id("cc_rimless_select_undefined_item_67").click()
        print("[2] Set to UK")

        #Filter only business approved
        self.page.get_by_text("Approved for business use").click()

        #Click on view more button
        for i in range(numSongs):
            self.page.get_by_test_id("cc_contentArea_viewmore_btn").get_by_text("View More").click()
            print(f"[3.{i}] Clicked view more button ({i+1}/{numSongs})")
        print("[4] End click view more button")
        urls = []

        print(getSongs)
        for j in range(2,getSongs):
            self.page.locator(f"div:nth-child({j}) > div > .ItemCard_soundItemContainer__GUmFb > .ItemCard_infoContentContainer__GbSoY > .ItemCard_leftContent__aA4ra > .ItemCard_coverIcon__Xu6zA").click()
            urls.append(re.search('''<audio src="(.*?)"''',self.page.content()).group(1))

        print(urls)
        self.page.wait_for_timeout(30000)
        return urls
    
    def tiktokSongsVideoUrl(self,numSongs=10):

        #Determine how many times you need to click on view more
        getSongs=numSongs
        numSongs-=3
        numSongs//=3
        if numSongs%3!=0:
            numSongs+=1

        #Open the page
        self.page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/music/pc/en")

        # [1] Change region
        self.page.click('span[data-testid="cc_rimless_select_undefined"]')
        print("[1] Region changed")

        # [2] Set to UK
        self.page.get_by_placeholder("Start typing or select from the list").click()
        self.page.get_by_placeholder("Start typing or select from the list").fill("united kin")
        self.page.get_by_test_id("cc_rimless_select_undefined_item_67").click()
        print("[2] Set to UK")

        #Click on view more button
        for i in range(numSongs):
            self.page.get_by_test_id("cc_contentArea_viewmore_btn").get_by_text("View More").click()
            print(f"[3.{i}] Clicked view more button ({i+1}/{numSongs})")
        print("[4] End click view more button")
        urls = []

        print(getSongs)
        for j in range(2,getSongs):
            try:
                self.page.locator(f"div:nth-child({j}) > div > .ItemCard_soundItemContainer__GUmFb > .ItemCard_infoContentContainer__GbSoY > .ItemCard_leftContent__aA4ra > .ItemCard_coverIcon__Xu6zA").click()
                urls.append(re.findall('''cite="(.*?)"''',self.page.content()))
                self.page.locator(".PaginationModal_closeIcon__L4jHA").click()
            except:
                break
        return urls





