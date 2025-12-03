# 登入myself

import requests


def get_http(url):

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    payload = {
        'formhash': '385ead7e',
        'referer': 'https://myself-bbs.com/portal.php',
        'loginfield': 'username',
        'username': 'account',
        'password': 'pawssord',
        'questionid': '0',

    }

    try:

        session = requests.session()
        r = session.post(url, headers=header, data=payload,
                         timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        r = session.get('https://myself-bbs.com/portal.php')
        return r.text  # 顯示網頁內容
    except:
        return "發生異常"


url = 'https://myself-bbs.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=L5nJu&inajax=1'
print(get_http(url))
