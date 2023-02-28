from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 设置Microsoft Edge Driver的路径
edge_driver_path = 'G:\GitHub\learn\selenium\webDrive\edgedriver_win32\msedgedriver.exe'

# 创建Microsoft Edge浏览器实例
driver = webdriver.Edge(executable_path=edge_driver_path)

# 打开Google登录页面
driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')

# 输入用户名
username = driver.find_element_by_name('identifier')
username.send_keys('rgps45021@gmail.com')
username.send_keys(Keys.RETURN)
time.sleep(2)

# 输入密码
password = driver.find_element_by_name('password')
password.send_keys('tim62712tim62712')
password.send_keys(Keys.RETURN)
time.sleep(5)

# 检查是否成功登录
try:
    profile_button = driver.find_element_by_css_selector(
        '#gb > div.gb_Ud.gb_0d.gb_wd > div.gb_Vd.gb_0d.gb_wd.gb_xd.gb_4d.gb_6d.gb_Ad.gb_Fd > div.gb_Cd.gb_0d.gb_wd.gb_xd > div.gb_Md.gb_Pf.gb_0d.gb_wd')
    print("Login successful!")
except:
    print("Login failed.")

# 关闭浏览器
driver.quit()
