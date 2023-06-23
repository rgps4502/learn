import requests
import urllib
import time
from bs4 import BeautifulSoup


with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\body3.html', 'r', encoding="utf-8") as f:
    r = f.read()
soup = BeautifulSoup(r, 'html.parser')


def req(session, url, header, payload=None):
    # 如果payload參數沒有給就當作是get請求否則為post請求
    if payload == 'None':
        r = session.get(url, headers=header, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    else:
        r = session.post(url, headers=header, data=payload,
                         timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


def get_http(url):

    header = {
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 登入用的data
    login_payload = {
        'referer': 'https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2fordersummary.html',
        '__VIEWSTATE': '/wEPDwUKMTY0Nzg0NzU0N2RkcweFlpgG3cvff6LrQyzoJkQhxetcYszKQQlHepcyA3c=',
        'ctl00$RapidSSLContent$txtUsername': 'moon.cake988@gmail.com',
        'ctl00$RapidSSLContent$txtPassword': 'r9DgQ7HEKezbpct',
        'ctl00$RapidSSLContent$btnLogin': 'Login',
        '__VIEWSTATEGENERATOR': '5F89FC59',
        '__EVENTVALIDATION': '/wEdAAQjkL3jJcqYFrkHnvBRdsxAcO1dB7UA/''GyDQStrVSOCjHfNGizx3lC8jGKGqxi1PhAlY6eIPpktbY3NBsQ56uSJzyNWoPoZW2Kb0YAmoEVdDHE07pO3YOp2SYd5w0n6Nxk=',
    }
    try:
        session = requests.session()
        # 登入
        soup = req(session, url, header, login_payload)
        soup = req(
            session, 'https://cheapsslsecurity.com/client/entercsr.html?id=4717&ProductID=46&crid=6675780', header)
        VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
        VIEWSTATEGENERATOR = soup.find(id='__VIEWSTATEGENERATOR')['value']
        EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')['value']

        print(VIEWSTATE)
        print(VIEWSTATEGENERATOR)
        print(EVENTVALIDATION)

    except Exception as e:
        print(e)


url = 'https://cheapsslsecurity.com/quicklogin.aspx?isauth=false&ReturnUrl=%2fclient%2fordersummary.html'
# get_http(url)
create_url = 'https://cheapsslsecurity.com' + \
    soup.find(id='ucCheckoutOrders1_rptOrders_hrefCompleteOrder_0')[
        'href']
order = 'https://cheapsslsecurity.com' + \
    soup.find(class_='btnviewicon')['href']
print(order)
