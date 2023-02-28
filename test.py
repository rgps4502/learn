from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com/signup")
    page.goto("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
    page.get_by_role("button", name="繼續").click()
    page.get_by_role("combobox", name="電話國碼 ​香港 (+852)").click()
    page.get_by_text("香港 (+852)").nth(1).click()
    page.get_by_role("combobox", name="電話國碼 ​台灣 (+886)").click()
    page.get_by_text("香港 (+852)").nth(1).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
