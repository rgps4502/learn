from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.facebook.com/
    page.goto("https://www.facebook.com/")

    # Click [data-testid="open-registration-form-button"]
    # with page.expect_navigation(url="https://www.facebook.com/"):
    with page.expect_navigation():
        page.locator("[data-testid=\"open-registration-form-button\"]").click()

    # Click [placeholder="姓氏"]
    page.locator("[placeholder=\"姓氏\"]").click()

    # Fill [aria-label="名字"]
    page.locator("[aria-label=\"名字\"]").fill("你")

    # Click [aria-label="手機號碼或電子郵件"]
    page.locator("[aria-label=\"手機號碼或電子郵件\"]").click()

    # Click [aria-label="手機號碼或電子郵件"]
    page.locator("[aria-label=\"手機號碼或電子郵件\"]").click()

    # Fill [aria-label="手機號碼或電子郵件"]
    page.locator("[aria-label=\"手機號碼或電子郵件\"]").fill("85253656130")

    # Click [aria-label="設定密碼"]
    page.locator("[aria-label=\"設定密碼\"]").click()

    # Fill [aria-label="設定密碼"]
    page.locator("[aria-label=\"設定密碼\"]").fill("^-@>csXqNB-t")

    # Select 2000
    page.locator("[aria-label=\"年\"]").select_option("2000")

    # Select 8
    page.locator("[aria-label=\"月\"]").select_option("8")

    # Select 25
    page.locator("[aria-label=\"日\"]").select_option("25")

    # Check input[name="sex"] >> nth=2
    page.locator("input[name=\"sex\"]").nth(2).check()

    # Check input[name="sex"] >> nth=0
    page.locator("input[name=\"sex\"]").first.check()

    # Check input[name="sex"] >> nth=1
    page.locator("input[name=\"sex\"]").nth(1).check()

    # Check input[name="sex"] >> nth=0
    page.locator("input[name=\"sex\"]").first.check()

    # Click button[name="websubmit"]
    page.locator("button[name=\"websubmit\"]").click()

    # Click button[name="websubmit"]
    page.locator("button[name=\"websubmit\"]").click()

    # Go to https://www.facebook.com/confirmemail.php?next=https%3A%2F%2Fwww.facebook.com%2F&__req=d
    page.goto("https://www.facebook.com/confirmemail.php?next=https%3A%2F%2Fwww.facebook.com%2F&__req=d")

    # Click text=再次發送簡訊
    page.locator("text=再次發送簡訊").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
