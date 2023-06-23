# -*- coding: utf-8 -*-
import requests
import os
import re
pathd = os.path.split(os.path.realpath(__file__))[0]


response = requests.get("https://www.sslproxies.org/")

proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+',
                       response.text)  # 「\d+」代表數字一個位數以上

valid_ips = []
for index, ip in enumerate(proxy_ips):
    try:
        if index <= 100:  # 驗證30組IP
            result = requests.get('https://ip.seeip.org/jsonip?',
                                  proxies={'http': ip, 'https': ip},
                                  timeout=5)
            print(result.json())
            valid_ips.append(ip)
    except:
        print(f"{ip} invalid")

with open(pathd+'/proxy_list.txt', 'w') as file:
    for ip in valid_ips:
        file.write(ip + '\n')
    file.close()
