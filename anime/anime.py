# * -*- coding: utf-8 -*-
from typing import NewType, Text
import requests
import time
from bs4 import BeautifulSoup


def get_http(url):
    try:
        session = requests.session()
        r = session.get(url, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼是正確的
        return r.text  # 顯示網頁內容
    except:
        print('1.連線失敗一分後重新嘗試')
        time.sleep(60)
        return get_http(url)  # 顯示網頁內容


def data():
    # beautiflusoup的方法
    soup = BeautifulSoup(get_http(url), "lxml")
    title = soup.find("div", id='portal_block_951_content')  # 尋找新翻的div,id
    titles = title.find(["style='width: 180px;'", 'ul'])  # 尋找div裡面的元素
    item = []
    item.insert(0, '')
    for name in titles:
        if name != None:
            # 取得<a>標籤的連結文字getText()方法(Method) 標籤底下所有<p>標籤select_one()方法進行選取
            item += [(name.select_one('p').getText())]
    return item


def sendmessage(message):
    headers = {
        "Authorization": "Bearer " + "KZuA1PCElIXss7soRvLTTr4Y3m5GSXjSyjye0gSMhFv",
        "Content-Type": "application/x-www-form-urlencoded"}
    params = {"message": message}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  # 200


url = 'https://myself-bbs.com/portal.php'
oldDate = data()
all_list = oldDate
message = ('\n'.join(map(str, oldDate)))  # 打印出換行的列表
sendmessage(message)
while(True):
    while(True):
        time.sleep(300)
        newDate = data()
        if newDate != oldDate:
            # 比較打印出在總表list不相同的
            Compareddf = [y for y in (oldDate+newDate) if y not in all_list]
            for newan in Compareddf:
                all_list.insert(1, newan)  # 把新的插入總表做後續比較用
                all_list.pop()  # 移除總表的最後一個保持15個
            Compareddf.insert(0, '')
            message = ('\n'.join(map(str, Compareddf)))
            sendmessage(message)
            oldDate = newDate
            break
        # print('這5分鐘沒有更新')
