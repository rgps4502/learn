import requests
import json

session = requests.session()


def ibon(session, url):

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    param = {
        'q': 'python'
    }

    try:

        r = session.get(url, headers=header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text)
    except:
        "連線失敗"


url_ibon = 'https://ticket.ibon.com.tw/'
url2 = 'https://huiwan.ibon.com.tw/Huiwan/LoginHuiwan/UserLogin.aspx?taxid=464939254&targeturl=http://ticket.ibon.com.tw'
url = 'https://huiwan.ibon.com.tw/huiwan/member/memberlogin.aspx?taxid=464939254&targeturl=http://ticket.ibon.com.tw&LoginType=OP'
ibon(session, url_ibon)
print('===================')
ibon(session, url2)
print('===================')
print(ibon(session, url))
