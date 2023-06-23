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


def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                # print(e)
                time.sleep(2)
                attempts += 1
                if attempts == 3:
                    return None

    return retry_wrapper


@retry
def test_ip(url, proxy_ip=None, cont=None):
    header = {
        'Cache-Control': 'max-age = 5',
        "User-Agent": user_agent.random,
    }

    proxy = {"http": proxy_ip}

    return requests.get(url=url, headers=header, timeout=6, proxies=proxy).text


def use_ip(res):
    soup = BeautifulSoup(res, 'html.parser')
    try:
        use_ip = str(soup.select_one(
            'body > b > span').get_text().replace('\n', ''))
        print(cont, ' 你使用的ip是:', use_ip)
    except AttributeError as e:
        pass


if __name__ == '__main__':
    url = "http://www.whatismyip.com.tw/"
    cont = 0
    for ip in proxy_ips:
        # 使用的代理ip地址
        res = test_ip(url, proxy_ip=ip, cont=cont)
        cont = cont+1
        if res != None:
            res = use_ip(res)
        else:
            print('第', cont, '失敗', ip)
