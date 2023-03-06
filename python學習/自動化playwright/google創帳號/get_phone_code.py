import time
import requests
import sys


headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_token():
    params = {
        'name': 'pipi090301',
        'password': 'A1B2C3D4@@'
    }
    url = 'https://smsn.szfang.tw/api/login'
    response = requests.get(url, headers=headers, params=params)
    return response.json()['api_token']


# 獲取電話
def get_phone_message(api_token):
    params = {
        'api_token': api_token,
        'projectId': 19
    }
    url = 'https://smsn.szfang.tw/api/getNumber'
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # 如果响应码不为 200，会抛出异常
        data = response.json()
    except (requests.exceptions.RequestException, KeyError):
        print('獲取電話號碼失敗')
    finally:
        return data


# 獲取電話號碼
def get_phone_number(token):
    phone_message = get_phone_message(api_token=token)
    if phone_message['msg'] == '獲取成功':
        phone_number = '+852'+phone_message['data']['number']
        orderid = phone_message['data']['orderid']
        print('獲取到號碼:', phone_message)
        return phone_number, orderid
    else:
        print('獲取號碼失敗', phone_message['msg'])
        sys.exit(1)


# 釋放手機號


def release_phone_number(token, orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/releaseNumber?'
    res = requests.get(url, headers=headers, params=params).json()
    print(res['msg'])


# 拉黑手機號
def deny_phone(token, orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/shieldNumber??'
    res = requests.get(url, headers=headers, params=params).json()
    print(res['msg'])
    # 獲取驗證碼


def get_phone_code(token, orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/getSmsContent?'
    count = 0
    while count < 10:
        res = requests.get(url, headers=headers, params=params).json()
        print(res)
        if res['msg'] == '正在获取驗證碼':
            time.sleep(2)
            count = count+1
            if count == 10:
                print('收不到驗證碼')
                # 釋放手機號
                release_phone_number(token, orderID)
                sys.exit(1)
        else:
            code = res['data']['messages'].split(' ')[0][2:]
            break
    return code


token = get_token()
for x in range(10):
    print(token)
    phone_number, orderid = get_phone_number(token)
    # release_phone_number(token, orderid)
    deny_phone(token, orderid)
    time.sleep(3)

# code = get_phone_code(token, orderid)
# print('獲取到的驗證碼:', code)
