# 登入cheapss

import requests
from bs4 import BeautifulSoup


def get_http(url, order):

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    payload = {
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
        r = session.post(url, headers=header, data=payload,
                         timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        r = session.get(
            'https://cheapsslsecurity.com/client/ordersummary.html')
        soup = BeautifulSoup(r.text, 'lxml')
        file_url = "https://cheapsslsecurity.com/client/orderdtl.html?orderdetailid=" + \
            order+"&isdownload=true"

        myfile = session.get(
            file_url)
        if myfile.status_code == 200:
            open('D:/下載/'+order+'.zip', 'wb').write(myfile.content)
        else:
            print('沒有下載成功')
        return soup.title  # 顯示網頁內容
    except:
        print(myfile.status_code)
        return "發生異常"


order = '443557'
url = 'https://cheapsslsecurity.com/quicklogin.aspx?isauth=false&ReturnUrl=%2fclient%2fordersummary.html'
print(get_http(url, order))
