from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="zh-CN")

    # Open new page
    page = context.new_page()

    # Go to https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button
    page.goto("https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button")

    # Go to https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin
    page.goto("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    # Click button:has-text("创建帐号")
    page.locator("button:has-text(\"创建帐号\")").click()

    # Click [aria-label="用户名"]
    page.locator("[aria-label=\"用户名\"]").click()

    # Click [aria-label="用户名"]
    page.locator("[aria-label=\"用户名\"]").click()

    # Click [aria-label="密码"]
    page.locator("[aria-label=\"密码\"]").click()

    # Click [aria-label="确认"]
    page.locator("[aria-label=\"确认\"]").click()

    # Click button:has-text("下一步")
    # with page.expect_navigation(url="https://accounts.google.com/signup/v2/webgradsidvphone?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&dsh=S-619839086%3A1658580281515481&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AKqFyY-v8gFYPlOVGa81vUWcBhZqdwmK52yMLJmAqvvLiKmhXJ7-OZN1YF0W-G43"):
    with page.expect_navigation():
        page.locator("button:has-text(\"下一步\")").click()

    # Click input[type="tel"]
    page.locator("input[type=\"tel\"]").click()

    # Click text=+886台湾 (+886)
    page.locator("text=+886台湾 (+886)").click()

    # Click text=香港 (+852)
    page.locator("text=香港 (+852)").click()

    # Click input[type="tel"]
    page.locator("input[type=\"tel\"]").click()

    # Click button:has-text("下一步")
    page.locator("button:has-text(\"下一步\")").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
