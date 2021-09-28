# * -*- coding: utf-8 -*-
from os import error
import requests
from requests.sessions import session
from All_account import cheapss

# 登入cheapss並返回下載地址


def login_cheapss(order):
    # 從All_account獲取帳號
    user = cheapss()[0]
    password = cheapss()[1]

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    payload = {
        'referer': 'https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2fordersummary.html',
        '__VIEWSTATE': '/wEPDwUKMTY0Nzg0NzU0N2RkcweFlpgG3cvff6LrQyzoJkQhxetcYszKQQlHepcyA3c=',
        'ctl00$RapidSSLContent$txtUsername': user,
        'ctl00$RapidSSLContent$txtPassword': password,
        'ctl00$RapidSSLContent$btnLogin': 'Login',
        '__VIEWSTATEGENERATOR': '5F89FC59',
        '__EVENTVALIDATION': '/wEdAAQjkL3jJcqYFrkHnvBRdsxAcO1dB7UA/''GyDQStrVSOCjHfNGizx3lC8jGKGqxi1PhAlY6eIPpktbY3NBsQ56uSJzyNWoPoZW2Kb0YAmoEVdDHE07pO3YOp2SYd5w0n6Nxk=',
    }

    try:
        # 登入的URL
        login_url = "https://cheapsslsecurity.com/quicklogin.aspx?isauth=false&ReturnUrl=%2fclient%2fordersummary.html"

        # 使用session函數可保留登入後訊息(cookies之類)
        session = requests.session()
        r = session.post(login_url, headers=header, data=payload,
                         timeout=120)  # 獲取網頁120秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼 EX:UTF-8

        # 下載鏈接(order會根據證書不同變換)
        file_url = "https://cheapsslsecurity.com/client/orderdtl.html?orderdetailid=" + \
            order+"&isdownload=true"
        file = session.get(file_url, timeout=120)  # 獲取網頁120秒為限
    except error as e:
        print(e, '請確認帳號或連線是否正常')
    # 返回get到的下載鏈接
    return file


def download(order):
    # 下載證書 判斷狀態碼200正常下載 500證書沒下來
    file = login_cheapss(order)
    try:
        if file.status_code == 200:
            open('D:/下載/'+order+'.zip', 'wb').write(file.content)
            mes = '證書下載成功'
        else:
            mes = '證書還沒下來'
    except error as e:
        return e
    return mes


if __name__ == '__main__':
    # 獲取order ID
    download('443557')
