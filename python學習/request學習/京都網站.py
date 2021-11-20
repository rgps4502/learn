import requests
from requests.exceptions import Timeout
from requests.models import get_cookie_header


def get(url):

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        session = requests.session()
        r = session.get(url, headers=header, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
#        r.encoding = r.apparent_encoding  # 用預測的解碼是正確的
        print(r.text[:400])  # 顯示網頁內容
    except:
        return "發生異常"


url = 'https://item.jd.com/100018568412.html'
get(url)
