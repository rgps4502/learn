# -*- coding: utf-8 -*-
import requests
import os
import time
import random
from retry import retry
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
user_agent = UserAgent()
pathd = os.path.split(os.path.realpath(__file__))[0]

# 打開proxy ip清單
with open(pathd+'/proxy_list.txt', 'r') as file:
    proxy_ips = file.read().splitlines()


@retry(exceptions=Exception, tries=3, delay=5)
def test_ip(proxy_ip, cont):
    header = {
        'Cache-Control': 'max-age = 5',
        "User-Agent": user_agent.random,
    }

    proxy = {"http": proxy_ip}
    # 訪問的網頁
    url = "http://www.whatismyip.com.tw/"
    try:
        res = requests.get(url=url, headers=header, timeout=6, proxies=proxy)
        soup = BeautifulSoup(res.text, 'html.parser')
        use_ip = str(soup.select_one(
            'body > b > span').get_text().replace('\n', ''))
        print(cont, ' 你使用的ip是:', use_ip)
        time.sleep(2)
    except Exception as e:
        print('第', cont, e)


cont = 1
for ip in proxy_ips:
    # 使用的代理ip地址
    test_ip(ip, cont)
    cont = cont+1
