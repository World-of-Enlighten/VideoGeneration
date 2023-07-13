from playwright.sync_api import Playwright, sync_playwright


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

    def tiktokHashtags(self,timeout=0):
        self.setup()
        self.page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en")

        # [1] Change region
        self.page.click('span[data-testid="cc_rimless_select_undefined"]')
        print("[1] Region changed")

        # [2] Set to UK
        self.page.click('[placeholder="Start typing or select from the list"]')
        self.page.fill('[placeholder="Start typing or select from the list"]', "united kin")
        self.page.get_by_test_id("cc_rimless_select_undefined_item_68").click()
        print("[2] Set to UK")

        # [3] Change hashtags
        self.page.locator("#hashtagIndustrySelect").get_by_role("img").click()
        self.page.get_by_test_id("cc_single_select_undefined_item_8").get_by_text("Health").click()
        print("[3] Set to #health")

        # [4] View more hashtags
        for _ in range(3):
            self.page.get_by_test_id("cc_contentArea_viewmore_btn").get_by_text("View More").click()
        print("[4] Pressed view more button to get more hashtags")

        # [5] Getting hashtags
        health_hashtags = self.page.query_selector_all('.CardPc_titleText__RYOWo')
        print("[5] Got hashtags")
        for hashtag in health_hashtags:
            print(hashtag.inner_text())
        self.page.wait_for_timeout(timeout)
        self.teardown()

    def googleMaps(self,timeout=10000):
        #this function allows to check geolocation settings
        #you should click on button "Your location", otherwise it'll be your real location
        self.setup()
        self.page.goto("https://maps.google.com")
        self.page.wait_for_timeout(timeout)
        self.teardown()

    def regionTiktok(self,timeout=0):
        self.setup()
        self.page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en")
        self.page.wait_for_timeout(timeout)
        self.teardown()

    def browserOpen(self):
        self.setup()
        self.page.goto("https://google.com")
        while True:
            pass



with sync_playwright() as playwright:
    scraper = Scraper(playwright)
    scraper.tiktokHashtags()
