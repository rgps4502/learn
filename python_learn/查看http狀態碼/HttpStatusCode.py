#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
url: https://www.yangshengliang.com/seo-ji-shu/seo-jiaocheng/722.html
author: fedkey
"""

import requests
import sys


def getHttpStatusCode(url):
    # 添加一个user-agent,访问反爬虫策略严格的网站很有用
    userAgent = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
    timeOut = 4  # 请求超时时间设置为4秒
    try:
        request = requests.get(url, headers=userAgent, timeout=10)
        httpStatusCode = request.status_code
        return httpStatusCode

    except requests.exceptions.HTTPError as e:
        return e


if __name__ == "__main__":
    url = sys.argv[1]  # 执行程序接受url作参数
    status = getHttpStatusCode(url)
    print(status)
