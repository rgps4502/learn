import os
from playwright.sync_api import Playwright, sync_playwright, expect
# 獲取腳本執行目錄
path = os.path.abspath(os.path.dirname(__file__))
# 截圖


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.boce.com/http
    page.goto("https://www.boce.com/http")

    # Click a:has-text("登录") >> nth=1
    with page.expect_popup() as popup_info:
        page.locator("a:has-text(\"登录\")").nth(1).click()
    page1 = popup_info.value

    # Click [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").click()

    # Fill [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").fill("Gz39Yj8hfvCuUw2t")

    # Click [placeholder="手机号码\/邮箱地址"]
    page1.locator("[placeholder=\"手机号码\\/邮箱地址\"]").click(modifiers=["Meta"])

    # Fill [placeholder="手机号码\/邮箱地址"]
    page1.locator("[placeholder=\"手机号码\\/邮箱地址\"]").fill("13099438051")

    # Click button:has-text("登录")
    # with page1.expect_navigation(url="https://www.boce.com/user/#/dashboard"):
    with page1.expect_navigation():
        page1.locator("button:has-text(\"登录\")").click()

    # Close page
    page1.close()

    for domain in domains:
        # Click [placeholder="请输入有效的URL地址"]
        page.locator("[placeholder=\"请输入有效的URL地址\"]").click()

        # Fill [placeholder="请输入有效的URL地址"]
        page.locator("[placeholder=\"请输入有效的URL地址\"]").fill(str(domain))

        # Click text=检测一下
        # with page.expect_navigation(url="https://www.boce.com/http/918gg.vip"):
        with page.expect_navigation():
            page.locator("text=检测一下").click()

        # 等待text=已检测结束 視窗出現 等待50秒
        page.wait_for_selector("text=已检测结束", state='attached', timeout=50000)
        # page.locator("text=已检测结束").click()

        # # 截圖 Click canvas 下載
        element_handle = page.query_selector("//canvas")  # 按照元素截图
        element_handle.screenshot(path=path+'\{0}.png'.format(domain))

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


domains = ["918gg.vip", "918ucc.com", "google.com"]
with sync_playwright() as playwright:
    run(playwright)
