import requests


def get_http(url):
    try:

        session = requests.session()
        r = session.get(url, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼是正確的
        return r.text  # 顯示網頁內容
    except:
        return "發生異常"


url = 'https://myself-bbs.com/portal.php'
print(get_http(url))
