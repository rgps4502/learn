import requests
import datetime
from bs4 import BeautifulSoup

session = requests.session()


def verify_google(email):
    session.headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }

    # 執行 post 請求
    data = {
        'yp': 'FZwxlBGp4ZmH1Amt2Zwt3ZmV',
        'login': email
    }
    url = 'https://yopmail.com/zh/'
    res = session.post(url, data=data)
    account = str(email).split('@yopmail.com')[0].lower()
    # 將 Set-Cookie 中的 cookies 添加到會話對象中
    cookies_str = f'yc=KZGx4AmZmAGxmZmH0ZQVmAQZ; ycons=WYuSjAOss65KE5fneVrtdZv6/EunAih/W6j1m4ZVe9g; compte={account}; ywm={account}; yses=ooPUM/OTTHjpnIauQmSFIH4ZGqN9M9ZGzsYGP2wiv6KaBDfTJcJUsxDcJvzxeTr+; ytime=0:5'

    cookies = {}
    for cookie in cookies_str.split(';'):
        cookie = cookie.strip()
        if cookie:
            key, value = cookie.split('=', 1)
            cookies[key] = value

    # 執行 get 請求
    url = f'https://yopmail.com/zh/inbox?login={account}&p=1&d=&ctrl=&yp=FZwxlBGp4ZmH1Amt2Zwt3ZmV&yj=RAQxlZmx0BQx4ZGZmZGx5ZQR&v=7.0&r_c=&id='
    res = session.get(url, cookies=cookies)

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    # 找到所有class屬性為lmh-header的元素
    latest_time = None
    latest_code = None

    for m in soup.find_all('div', {'class': 'm'}):
        time_elem = m.find('span', {'class': 'lmh'})
        if time_elem is not None:
            time_str = time_elem.text.strip()
            try:
                time = datetime.datetime.strptime(time_str, '%H:%M')
            except ValueError:
                continue
            if latest_time is None or time > latest_time:
                latest_time = time
                code_elem = m.find('div', {'class': 'lms'})
                if code_elem is not None and '驗證碼' in code_elem.text:
                    latest_code = code_elem.text.strip().split('：')[1]
                elif code_elem is not None and 'Email verification code' in code_elem.text:
                    latest_code = code_elem.text.strip().split(':')[1]

    if latest_code is not None:
        print(f"最新的Google驗證碼為 {latest_code}.")
        return latest_code
    else:
        print("沒有最新的Google驗證碼.")


if __name__ == '__main__':
    email = 'tgy4qNC101@yopmail.com'
    verify_google(email)
