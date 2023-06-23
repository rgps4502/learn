from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as playwright:
    # 设置浏览器选项
    browser = playwright.firefox.launch(headless=False, proxy={
        'server': 'http://5.78.68.101:8080'})
    context = browser.new_context()
    # 创建一个新的页面
    page = context.new_page()
    # 访问Google登录页面
    page.goto('https://accounts.google.com/signin')
    # 等待登录表单出现
    page.wait_for_selector('#identifierId')
    # 输入用户名
    page.fill('#identifierId', 'rgps45021@gmail.com')
    # 点击下一步按钮
    page.click('#identifierNext')
    # 等待密码输入框出现
    page.wait_for_selector('input[name="Passwd"]')
    # 输入密码
    page.fill('input[name="Passwd"]', 'tim62712tim62712')
    # 点击下一步按钮
    page.click('#passwordNext')
    # 等待登录完成
    page.wait_for_selector('#gbq1', state='visible')
    # 登录完成后，做其他操作
    # ...
    # 关闭浏览器
    browser.close()
