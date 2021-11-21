
import requests
import pandas
from lxml import etree
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

# 查詢公司的基金購買的股票有哪幾隻
# 判斷出公司基金購買重複次數最高的股票

# 訪問查詢公司股票網頁


def req(session, url, header, payload=None):
    try:
        # 如果payload參數沒有給就當作是get有給就當作是Post
        if payload == None:
            r = session.get(url, headers=header, timeout=60)  # get網頁60秒為限
            r.raise_for_status()  # 如果狀態碼不是200引發HTTPERROR異常
            r.encoding = r.apparent_encoding  # 預測解碼
            soup = BeautifulSoup(r.text, 'html.parser')
            return soup
        else:
            r = session.post(url, headers=header, data=payload, timeout=60)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            return soup
    except ConnectionError as ce:
        print(ce)
    except BaseException as f:
        print(f)


def search_stock(session, url):
    # 定義header
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    # get獲取post所需data
    soup = req(session, url, header)
    VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
    VIEWSTATEGENERATOR = soup.find(id='__VIEWSTATEGENERATOR')['value']
    EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')['value']
    # 選擇年月份
    month = soup.select_one('#ctl00_ContentPlaceHolder1_ddlQ_YM').select_one(
        'option[selected="selected"]')['value']
    # 選擇公司
    company = soup.select_one(
        '#ctl00_ContentPlaceHolder1_ddlQ_Comid1').select_one('option[selected="selected"]')['value']

    # 定義data
    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        '__EVENTVALIDATION': EVENTVALIDATION,
        'ctl00$ContentPlaceHolder1$ddlQ_YM': month,
        'ctl00$ContentPlaceHolder1$rdo1': 'rbComCL',
        'ctl00$ContentPlaceHolder1$ddlQ_Comid1': company,
        'ctl00$ContentPlaceHolder1$ddlQ_Class1': 'AA1',
        'ctl00$ContentPlaceHolder1$BtnQuery': '查詢'
    }
    # 查詢公司+國內投資股票類型
    soup = req(session, url, header, data)
    # with open('G:\\GitHub\\learn\\python學習\\股票\\respon.html', 'w', encoding='UTF-8') as f:
    # f.write(str(soup.prettify()))
    # 獲取基金名稱
    tag1 = soup.select_one('.DTHeader').getText()
    print(tag1)
    tag_name = soup.select(
        '.DTeven')[4]
    tag_name1 = soup.select(
        '.DTeven')[14]
    tag_name2 = soup.select(
        '.DTeven')[24]
    # dfs = pandas.read_html(tag_name)
    print(tag_name)
    print(tag_name1)
    print(tag_name2)


# 定義網頁
url = 'https://www.sitca.org.tw/ROC/Industry/IN2629.aspx?pid=IN22601_04'
# 定義重新連線次數3
test_connect = HTTPAdapter(max_retries=3)
session = requests.session()
session.mount(url, test_connect)
search_stock(session, url)
