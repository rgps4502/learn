from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com/signup")
    page.get_by_role("link", name="安全性", exact=True).click()
    page.get_by_placeholder("<您的使用者名稱>@example.com").click()
    page.get_by_placeholder("<您的使用者名稱>@example.com").click()
    page.get_by_placeholder(
        "<您的使用者名稱>@example.com").fill("3WQCVcS5o1@yopmail.com")
    page.get_by_role("link", name="備援電話號碼").click()
    page.get_by_role("button", name="移除電話號碼").click()
    page.get_by_role("button", name="移除電話號碼").click()
    page.get_by_role("button", name="返回").click()
    page.get_by_role("link", name="備援電子郵件", exact=True).click()
    page.get_by_role("link", name="Security", exact=True).click()
    page.get_by_role("link", name="Security", exact=True).click()
    page.get_by_role("link", name="Recovery phone").click()
    page.get_by_role("button", name="Remove phone number").click()
    page.get_by_role("button", name="Remove number").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("link", name="Recovery email").click()
    page.get_by_placeholder("you@example.com").click()
    page.get_by_placeholder("you@example.com").click()
    page.get_by_placeholder(
        "you@example.com").fill("tgy4qNC10@yopmail.comtgy4qNC10@yopmail.com")
    page.get_by_placeholder("you@example.com").press("Control+z")
    page.get_by_placeholder("you@example.com").fill("tgy4")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
