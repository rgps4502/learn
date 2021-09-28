import requests


def search_IP(url):
    header = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    session = requests.Session()
    r = session.get(url+'219.91.105.236&action=2', headers=header, timeout=30)
    r.encoding = r.apparent_encoding
    print(r.text[5000:])  # 返回文本的最後500字
    print(r.url)


url = 'https://ip138.com/iplookup.asp?ip='
search_IP(url)
