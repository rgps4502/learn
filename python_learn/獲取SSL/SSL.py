import whois
import pandas as pd
from datetime import datetime
import requests
from pprint import pprint


def domainStatus(domain):
    code = requests.get('https://' + domain).status_code
    if code == 200:
        state = '🟢'
    else:
        state = '🔴'

    return state + ' ' + str(code)


domains = [
    'myself-bbs.com'
]

for domain in domains:
    print(domainStatus(domain))
    print('ICANN 註冊資料：')
    pprint(whois.whois(domain), width=1)
