
import requests
import subprocess
import os
import json
import datetime
session = requests.session()
# 獲取腳本執行目錄
path = os.path.abspath(os.path.dirname(__file__))
# 獲取每日數據


def login():

    url = "https://dashboard.honeygain.com/api/v1/users/tokens"

    payload = json.dumps({
        "email": "rgps45021@gmail.com",
        "password": "tim62712tim62712"
    })
    headers = {
        'authority': 'dashboard.honeygain.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'content-type': 'application/json',
        'cookie': 'G_ENABLED_IDPS=google',
        'origin': 'https://dashboard.honeygain.com',
        'referer': 'https://dashboard.honeygain.com/login',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response = session.post(url, headers=headers, data=payload)
    response = response.json()
    # print(response['data']['access_token'])
    return response['data']['access_token']


# 獲取drive狀態
def dreve_status(token):

    url = "https://dashboard.honeygain.com/api/v2/devices"

    payload = {}
    headers = {
        'authority': 'dashboard.honeygain.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'authorization': 'Bearer {0}'.format(token),
        'referer': 'https://dashboard.honeygain.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response = session.get(url, headers=headers, data=payload).json()

    status_list = []
    for status in response['data']:
        status_list.append(status['status'])

    # print(status_list)

    # 如果狀態都不一樣就重啟
    if (len(set(status_list))) == 1:
        # print(subprocess.getstatusoutput('systemctl restart docker')[1])
        pass


def get_bonus(token):
    url = "https://dashboard.honeygain.com/api/v1/notifications?user_id=6ca4cd83-b673-4ecd-9141-785fe9dcb7bf"

    payload = {}
    headers = {
        'authority': 'dashboard.honeygain.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'authorization': 'Bearer {0}'.format(token),
        'referer': 'https://dashboard.honeygain.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response = session.get(url, headers=headers, data=payload)
    # print(response.json())

    return response


# 小蜜蜂# 點擊每日
def post_bones(token, campaign_id, hash_id):
    url = "https://dashboard.honeygain.com/api/v1/notifications/{0}/actions".format(
        hash_id)

    payload = json.dumps({
        "campaign_id": campaign_id,
        "action": "triggered",
        "user_id": "6ca4cd83-b673-4ecd-9141-785fe9dcb7bf"
    })
    headers = {
        'authority': 'dashboard.honeygain.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'authorization': 'Bearer {0}'.format(token),
        'content-type': 'application/json',
        'origin': 'https://dashboard.honeygain.com',
        'referer': 'https://dashboard.honeygain.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response = session.post(url, headers=headers, data=payload)

    # print(response.text)


# 把獲取到的分數Post出去
def post_bones2(token1):

    url = "https://dashboard.honeygain.com/api/v1/contest_winnings"

    payload = {}
    headers = {
        'authority': 'dashboard.honeygain.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-TW,zh;q=0.9',
        'authorization': 'Bearer {0}'.format(token1),
        'content-length': '0',
        'origin': 'https://dashboard.honeygain.com',
        'referer': 'https://dashboard.honeygain.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    response = session.post(url, headers=headers, data=payload)

    # print(response.text)
    if response.status_code == 200:
        # 刪除昨天的檔案
        delet_yesterday_path()
        # 創建今天的檔案
        touch_path(response.text)


def everyday(token):
    res = get_bonus(token)
    if res.status_code == 200:
        res = res.json()['data']
        if res == []:
            pass
        else:
            campaign_id = res[0]['campaign_id']
            hash_id = res[0]['hash']
            # print(campaign_id)
            # print(hash_id)
            # post_bones(token, campaign_id, hash_id)
            # 把獲取到的分數Post出去
            post_bones2(token1)


# 創建今天的txt文件用來區分是否執行過bones
def touch_path(response):
    today = int(datetime.datetime.now().strftime('%d'))
    # print(today)

    with open('{0}/{1}.txt'.format(path, today), 'w', encoding='UTF-8') as f:
        f.write(str(response))


# 刪除昨天的txt檔案
def delet_yesterday_path():
    yesterday = int((datetime.datetime.now() -
                     datetime.timedelta(days=1)).strftime("%d"))
    # print(yesterday)
    try:
        os.remove(path+'/{0}.txt'.format(yesterday))
    except OSError as e:

        with open('{0}/{1}.txt'.format(path, today), 'w', encoding='UTF-8') as f:
            f.write(str(e))
        pass


if __name__ == '__main__':
    subprocess.getoutput('ntpdate -s time.stdtime.gov.tw;clock -w')
    print(subprocess.getoutput('date'))
    today = int(datetime.datetime.now().strftime('%d'))
    # 察看是今日是否執行過
    file_exiet = os.path.isfile('{0}/{1}.txt'.format(path, today))
    if file_exiet != True:

        # 登入獲取token
        token1 = login()

        # 看設備狀態
        # dreve_status(token1)

        everyday(token1)
