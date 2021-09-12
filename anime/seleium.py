from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
import requests


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

browser = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options,
    desired_capabilities=DesiredCapabilities.CHROME,
)
#browser = webdriver.Chrome(options = options)


def sendmessage(message):
    headers = {
        "Authorization": "Bearer " + "KZuA1PCElIXss7soRvLTTr4Y3m5GSXjSyjye0gSMhFv",
        "Content-Type": "application/x-www-form-urlencoded"}
    params = {"message": message}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  # 200


browser.set_page_load_timeout(60)
browser.get('https://myself-bbs.com/portal.php')

all_a = browser.find_elements_by_id("portal_block_951_content")
all_a = [i.text for i in all_a]
oldate = all_a
oldate.insert(0, '')
message = ('\n'.join(map(str, oldate)))

sendmessage(message)


browser.quit()
