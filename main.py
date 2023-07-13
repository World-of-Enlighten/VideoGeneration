from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
    geolocation={"longitude": 51.136502, "latitude": 22.413220},
    permissions=["geolocation"]
    )
    page = context.new_page()
    page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en")
    
    #change region
    page.get_by_role("button", name="Morocco").click()
    print("[1] Region changed")

    #set to uk
    page.get_by_placeholder("Start typing or select from the list").click()
    page.get_by_placeholder("Start typing or select from the list").fill("united kin")
    page.get_by_test_id("cc_rimless_select_undefined_item_68").click()
    print("[2] Set to UK")

    #change hashtags
    page.locator("#hashtagIndustrySelect").get_by_role("img").click()
    page.get_by_test_id("cc_single_select_undefined_item_8").get_by_text("Health").click()
    print("[3] Set to #health")

    #viewing more hashtags
    for i in range(3):
        page.get_by_test_id("cc_contentArea_viewmore_btn").get_by_text("View More").click()
    print("[4] pressing on view more button to get more hashtags")

    #getting hashtags
    health_hashtags = page.query_selector_all('.CardPc_titleText__RYOWo')
    print("[5] Got hashtags")
    for hashtag in health_hashtags:
        print(hashtag.inner_text())
    

    page.wait_for_timeout(10000)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

#CardPc_titleText__RYOWo
# playwright codegen demo.playwright.dev/todomvc  