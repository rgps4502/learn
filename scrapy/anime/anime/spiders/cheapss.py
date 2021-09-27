import re
from lxml.html import parse
import requests
import json
import scrapy
from scrapy import FormRequest
import time
from bs4 import BeautifulSoup
from scrapy.http import headers


def search(response):
    print(response.body)


class CheapssSpider(scrapy.Spider):
    name = 'cheapss'
    # allowed_domains = ['cheapsslsecurity.com']

    start_urls = [
        'https://cheapsslsecurity.com/quicklogin.aspx?isauth=false&ReturnUrl=%2fclient%2fordersummary.html']

    # login_url = "https://cheapsslsecurity.com/client/orders.html"

    def parse(self, response):

        payload = {
            'referer': 'https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2fordersummary.html',
            '__VIEWSTATE': '/wEPDwUKMTY0Nzg0NzU0N2RkcweFlpgG3cvff6LrQyzoJkQhxetcYszKQQlHepcyA3c=',
            'ctl00$RapidSSLContent$txtUsername': 'moon.cake988@gmail.com',
            'ctl00$RapidSSLContent$txtPassword': 'r9DgQ7HEKezbpct',
            'ctl00$RapidSSLContent$btnLogin': 'Login',
            '__VIEWSTATEGENERATOR': '5F89FC59',
            '__EVENTVALIDATION': '/wEdAAQjkL3jJcqYFrkHnvBRdsxAcO1dB7UA/''GyDQStrVSOCjHfNGizx3lC8jGKGqxi1PhAlY6eIPpktbY3NBsQ56uSJzyNWoPoZW2Kb0YAmoEVdDHE07pO3YOp2SYd5w0n6Nxk=',
        }

        cookie = {
            'cookie': '.ASPXANONYMOUS=lvsRivHp1wEkAAAAZTYwYjcyMzEtNjAxMy00N2ViLTg4ZDctNDQ3Mjc2ZWIyMDY0BgeNDgYXPymARB6UQHxj7spFIXJsv9lXRLCmwHnfnkA1; ASP.NET_SessionId=vqqkeefk3zbxpco2zvdagxxw; _ga=GA1.2.1096757397.1632720174; _gid=GA1.2.1611250389.1632720174; _gcl_au=1.1.504918032.1632720174; BlockPop=true; _hjid=f2d223e8-34e2-4fb3-a03c-1ce6eca81dbd; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0; _hjIncludedInPageviewSample=1; _gali=btnLogin'
        }
        yield scrapy.FormRequest.from_response(response, formdata=payload, meta={'cookie': cookie}, callback=self.after_login)

    def after_login(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        print(soup.title)
        file_url = "https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2forderdtl.html%3forderdetailid%3d443556%26isdownload%3dtrue&orderdetailid=443557&isdownload=true"
        file = requests.get(file_url, allow_redirects=True)
        open('D:/下載/123.zip', 'wb').write(file.content)
