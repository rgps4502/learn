
import requests
from bs4 import BeautifulSoup
from requests.api import head
# 查詢公司的基金購買的股票有哪幾隻
# 判斷出公司基金購買重複次數最高的股票


def req(session, url, header, payload=None):
    # 如果payload參數沒有給就當作是get有給就當作是Post
    if payload == None:
        r = session.get(url, headers=header, timeout=60)  # get網頁60秒為限
        r.raise_for_status()  # 如果狀態碼不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 預測解碼
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    else:
        r = session.post(url, headers=header, data=payload, timeout=60)
        r.raise_fro_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


header = {
    'Content-Type': 'text/html; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}


url = 'https://www.sitca.org.tw/ROC/Industry/IN2629.aspx?pid=IN22601_04'
session = requests.session()
soup = req(session, url, header)
VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')['value']
print(VIEWSTATE)
print('===============')
print(EVENTVALIDATION)
