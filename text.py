from selenium import webdriver

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开Google登录页面
driver.get('https://accounts.google.com/signin')

# 填写用户名
username = driver.find_element_by_id('identifierId')
username.send_keys('你的用户名')

# 单击“下一步”按钮
next_button = driver.find_element_by_id('identifierNext')
next_button.click()

# 等待页面加载完成
driver.implicitly_wait(10)

# 填写密码
password = driver.find_element_by_name('password')
password.send_keys('你的密码')

# 单击“下一步”按钮
next_button = driver.find_element_by_id('passwordNext')
next_button.click()

# 等待页面加载完成
driver.implicitly_wait(10)

# 访问需要登录的页面
driver.get('https://www.google.com/')

# 打印页面内容
print(driver.page_source)

# 关闭浏览器
driver.quit()
