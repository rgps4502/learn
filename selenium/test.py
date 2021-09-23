
from os import error
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')  # 不添加會有奇怪抱錯
browser = webdriver.Chrome(chrome_options=options)
browser.implicitly_wait(10)
browser.get("https://www.google.com")
inputElement = browser.find_element_by_name("q")
inputElement.send_keys("Selenium")
inputElement.submit()
find = '//*[@id="lo-post-page-navbar-sign-in-button"]/div/span/button'

# try:
#     element = WebDriverWait(browser, 60).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, find)))
#     print('yes')
# except:
#     print('沒找到')

try:
    element = browser.find_element_by_xpath(find)
    element.click()
except:
    browser.refresh()
    browser.find_element_by_class_name('LC20lb').click()
    element = browser.find_element_by_xpath(find)
    element.click()
else:
    print(browser.title)
