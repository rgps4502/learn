
from os import error
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')  # 不添加會有奇怪抱錯
browser = webdriver.Chrome(chrome_options=options)
browser.implicitly_wait(3)
url = "https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2forderdtl.html%3forderdetailid%3d443556%26isdownload%3dtrue&orderdetailid=443557&isdownload=true"
browser.get(url)


# try:
#     element = WebDriverWait(browser, 60).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, find)))
#     print('yes')
# except:
#     print('沒找到')

try:
    browser.find_element_by_name(
        "ctl00$RapidSSLContent$txtUsername").send_keys("moon.cake988@gmail.com")
    time.sleep(1)
    browser.find_element_by_id("txtPassword").send_keys(
        "r9DgQ7HEKezbpct")
    time.sleep(1)
    browser.find_element_by_xpath('//*[(@id = "btnLogin")]').click()


finally:
    txt = browser.page_source
    # browser.quit()
