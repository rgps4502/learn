from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button
    page.goto("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button")

    # Go to https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin
    page.goto("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    # Click button:has-text("建立帳戶")
    page.locator("button:has-text(\"建立帳戶\")").click()

    # Click li[role="menuitem"]:has-text("建立個人帳戶")
    # with page.expect_navigation(url="https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&dsh=S-922018370%3A1659262558225204&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"):
    with page.expect_navigation():
        page.locator("li[role=\"menuitem\"]:has-text(\"建立個人帳戶\")").click()
    # expect(page).to_have_url("https://accounts.google.com/SignUp?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&dsh=S-922018370%3A1659262558225204&biz=false")

    # Click [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").click()

    # Fill [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").fill("}1`wzaoRE/$w")

    # Press z with modifiers
    page.locator("[aria-label=\"姓氏\"]").press("Control+z")

    # Click [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").click()

    # Fill [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").fill("曹杰志")

    # Click [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
