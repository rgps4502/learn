# 練習測試beatifulsoup
from os import pardir
import requests
from bs4 import BeautifulSoup


def bs():
    try:
        session = requests.session()
        r = session.get(url, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼是正確的
        demo = r.text
        # demo裡面的文本 用beautifulsoup 功能使用html.parser解析
        # 放一段HTML當HEADER
        soup = BeautifulSoup(
            demo, 'html.parser')
        # print(soup.head)  # 查看head
        # print(soup.head.contents)  # 查看他的兒子節點 (也就是title標籤)
        # print(soup.body.contents) #看body的兒子節點
        # print(len(soup.body.contents))  # 用len查看有幾個節點
        # print(soup.body.contents[1])  # 一共11個裡面看第一個兒子節點
        for child in soup.body.contents:  # 用for迴圈打印出所有兒子節點
                print(child)
    except:
        return "連線失敗"


url = 'https://www.icourse163.org/'
bs()
