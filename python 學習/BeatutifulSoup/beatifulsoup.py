# 練習測試beatifulsoup
from os import pardir
import requests
from bs4 import BeautifulSoup


def bs(url):
    try:
        session = requests.session()
        r = session.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        # demo裡面的文本 用beautifulsoup 功能使用html.parser解析
        soup = BeautifulSoup(demo, 'html.parser')
        # print(soup.prettify())  # 看解析後的text模樣
        # print(soup.h2)  # 看解析後的h2標籤
        # print(soup.input) #看解析後的input標籤
        # print(soup.input.parent.name)  # 看解析後的input 父標籤
        # print(soup.input.parent.parent.name)  # 看解析後的input 父父標籤
        # print(soup.a)  # 看解析後的a標籤
        tag = soup.div  # 看解析後div 定義tag
        # print(tag.attrs)  # 看標籤的屬性
        # print(tag.attrs['id'])  # 單看標籤的屬性對應valu
        print(type(tag.attrs))  # 看類型
    except:
        return "連線失敗"


url = 'https://mofanpy.com/tutorials/data-manipulation/scraping/requests/'
bs(url)
