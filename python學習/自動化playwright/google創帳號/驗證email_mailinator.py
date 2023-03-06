from playwright.sync_api import Playwright, sync_playwright
import time
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.mailinator.com/v4/public/inboxes.jsp?to=rriji7c2h")
    time.sleep(3)

    # 关闭浏览器
    browser.close()
