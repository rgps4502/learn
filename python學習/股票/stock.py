# -*- coding:utf-8 -*-
import requests
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


def search_stock(session, url, company):
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
    com = soup.find(
        id="ctl00_ContentPlaceHolder1_ddlQ_Comid")

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
    with open('G:\\GitHub\\learn\\python學習\\股票\\respon.html', 'w', encoding='UTF-8') as f:
        f.write(str(soup))
    # 獲取基金公司的數量(用字串'合計'做次數 幾家)
    tag_count = soup.select('td[colspan="9"]')
    stock_count = len(tag_count)
    # print(stock_count)

    # 獲取標得列表 他的表示由DTeven與DTodd組成
    stock_DTeven_list = soup.select('.DTeven')
    stock_DTodd_list = soup.select('.DTodd')
    # 定義出現標的次數清單
    stock_count_list = []
    # 定義要比較的標的清單
    stock_list = []
    # 定義出現標的代號(股票代號)
    stock_code_list = []
    # 獲取第一家基金的10個標列表(5個) 加入到標的清單  用第一家的10個標 去比較是否每一個公司基金都有購買同一個標
    x = 0
    for i in stock_DTeven_list:
        # 獲取股票代號
        if x in [3, 12, 21, 30, 39]:
            stock_code_list.append(i.getText())
            # 這個意思stock_DTeven_list[3]
        # 獲取股票清單
        elif x in [4, 13, 22, 31, 40]:
            stock_list.append(i.getText())
        x = x + 1

    # 獲取第一家基金的10個標列表(5個) 加入到標的清單
    r = 0
    for i in stock_DTodd_list:
        # 獲取股票代號
        if r in [2, 11, 20, 29, 38]:
            stock_code_list.append(i.getText())
        # 獲取股票清單
        elif r in [3, 12, 21, 30, 39]:
            stock_list.append(i.getText())
        r = r + 1

    # 將股票代號與股票作成字典
    stock_dict = dict(zip(stock_list, stock_code_list))

    # 用股票清單去找出出現次數的股票加入stock_count_list清單
    for stock in stock_list:
        for i in stock_DTeven_list:
            if stock == i.getText():
                stock_count_list.append(stock)
        for i in stock_DTodd_list:
            if stock == i.getText():
                stock_count_list.append(stock)
        # 比對出現次數是否跟stock_count 一致 (有幾家基金就有多少stock_count) 表示條件判斷100%出現
        if stock_count_list.count(stock) == stock_count:
            print(stock, stock_dict.get(stock))


# 定義網頁
url = 'https://www.sitca.org.tw/ROC/Industry/IN2629.aspx?pid=IN22601_04'
# 定義重新連線次數3
test_connect = HTTPAdapter(max_retries=3)
session = requests.session()
session.mount(url, test_connect)
# 選擇公司A0001~A0050
# company_list = ['A0001', 'A0003', 'A0004', 'A0005', 'A0006', 'A0007', 'A0008', 'A0009', 'A0010', 'A0011', 'A0012', 'A0014', 'A0015', 'A0016', 'A0017', 'A0018', 'A0020', 'A0021', 'A0022',
#                 'A0025', 'A0026', 'A0027', 'A0031', 'A0032', 'A0033', 'A0035', 'A0036', 'A0037', 'A0038', 'A0040', 'A0041', 'A0042', 'A0043', 'A0044', 'A0045', 'A0047', 'A0048', 'A0049', 'A0050']
company_list = ['A0001']
for company in company_list:
    print(company)
    search_stock(session, url, company)
    print("============")
