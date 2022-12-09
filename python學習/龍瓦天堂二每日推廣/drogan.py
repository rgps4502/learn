#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 龍瓦天堂二每日自動發推廣

import requests
import datetime
from bs4 import BeautifulSoup
session = requests.session()


def res(session, url, data=None):
    # 添加一个user-agent,访问反爬虫策略严格的网站很有用
    userAgent = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
    timeOut = 4  # 请求超时时间设置为4秒
    try:
        if data != None:
            request = session.post(url, headers=userAgent,
                                   data=data, timeout=10)
        else:
            request = session.get(url, headers=userAgent, timeout=10)
        return request.text

    except requests.exceptions.HTTPError as e:
        return e


if __name__ == "__main__":
    # 登入
    data = {
        'fastloginfield': 'username',
        'username': 'rgps4502',
        'password': 'tim62712',
        'quickforward': 'yes',
        'handlekey': 'ls'
    }
    url = 'https://hmsff.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'  # 登入論壇
    res(session, url, data)

    # 獲取論壇頁面資訊
    url = 'https://hmsff.com/thread-241-196-1.html'
    response = res(session, url, data)

    # 解析獲取hash
    soup = BeautifulSoup(response, 'html.parser')
    hash = soup.find('input', attrs={'name': 'formhash'})["value"]

    # 今天日期
    date = datetime.date.today().strftime("%m/%d")
    # 發文
    msg = f'''亞丁伺服器『薩維瓦天堂II』穩定不斷線獨家變身/卡片系統

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

SF版本：亞丁-領銜先鋒

SF位置：台灣

經驗倍率：5

金錢倍率：5

掉寶倍率：1

人數限制：無限制

詳細介紹：

伺服器名稱：薩維瓦天堂II伺服器版本：經典亞丁伺服器 穩定不斷線

註冊方式:無須註冊，首次登入即註冊

經驗值倍率：5

技能點數倍率：1

掉寶率：3

最大強化值：+30

Discord連結:https://discord.gg/VwzsrUN4TD

伺服器簡介：

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

1.全面下降怪物以及首領強度，讓您可以更輕鬆體驗遊戲

2.技能完整實裝，讓你體驗最精彩的打擊感

3.完整製作系統，讓你的冒險之路不再卡卡

4.完整實裝各式副本，讓你不再只是掛機無法與其他玩家互動

5.完整實裝收藏系統，讓有收藏嗜好的你更簡單達成

6.日後會持續完善遊戲內的系統以及開放新的副本

7.全新職業 先鋒登場

8.團隊承諾決不讓伺服器走向變態化的設置，以及朝令夕改誰強削弱誰的狀態

一律依照官方模式去做修正以及改動，

9.如有玩家良好建議可公開討論即評估施行方式

10.決不販售自製技能讓遊戲平衡失調

11.獨家全職業傳奇變身技能

12.獨家卡片系統

訪間充斥的各種魔改的天堂II，讓你無法完整體驗天堂II的魅力嗎

薩維瓦天堂II，決不會做過多的修改，也不會特別修改任何職業，用最原味的方式體驗天堂II

歡迎您的蒞臨，不需費用也可以完整體驗遊戲，盡在 薩維瓦天堂II

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

※最穩定的伺服器讓你上班掛到下班不斷現在下班後還可以有遊戲體驗※

經典亞丁 {date} 伊斯迪亞'''
    data = {
        'message': msg,
        'formhash': hash,
        'usesig':  '1',
        'subject': '',
    }
    url = 'https://hmsff.com/forum.php?mod=post&action=reply&fid=40&tid=241&extra=&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
    response = res(session, url, data)
#     # print(response)

    response = response.split(' ')[6]
#     # print(response)
    str1 = response
    str2 = "forum.php?"
#     # print(str1[str1.index(str2):-2])
    url = 'https://hmsff.com/'+str1[str1.index(str2):-2]
    print('帖子鏈接:'+url)

#     response = '''<?xml version="1.0" encoding="utf-8"?>
# <root><![CDATA[<script type="text/javascript" reload="1">if(typeof succeedhandle_fastpost=='function') {succeedhandle_fastpost('forum.php?mod=viewthread&tid=241&pid=287841&page=195&extra=#pid287841', '非常感謝，回復發佈成功，現在將轉入主題頁，請稍候……[ 點擊這裡轉入主題
# 列表 ]', {'fid':'40','tid':'241','pid':'287841','from':'','sechash':''});}</script>]]></root>'''
