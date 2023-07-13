from playwright.sync_api import Playwright, sync_playwright
from util.functions import *
import util.data as data

class Scraper:
    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None
        self.page = None

    def setup(self):
        self.browser = self.playwright.chromium.launch(headless=False)
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
        self.setup()
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
        self.setup()
        self.page.goto("https://maps.google.com")
        self.page.wait_for_timeout(timeout)
        self.teardown()

    def browserOpen(self):
        self.setup()
        self.page.goto("https://google.com")
        while True:
            pass



with sync_playwright() as playwright:
    scraper = Scraper(playwright)
    print(scraper.tiktokHashtags())
