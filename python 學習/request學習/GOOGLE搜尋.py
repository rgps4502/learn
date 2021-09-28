import requests
import json


def searc(url):

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    param = {
        'q': 'python'
    }

    try:
        session = requests.session()
        r = session.get(url, headers=header, params=param, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(len(r.text))  # 獲取字元
    except:
        "連線失敗"


url = 'https://www.google.com/search'
searc(url)
