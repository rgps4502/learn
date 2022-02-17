#!/usr/bin/env python3

import ssl
import socket
import requests
from dateutil import parser
import pytz

requests.packages.urllib3.disable_warnings()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def get_domain_content(domain):
    requests.packages.urllib3.disable_warnings()
    url = 'https://' + domain
    response = requests.get(url, verify=False).headers
    print(response)


def get_my_domain(mydomain):
    try:
        socket.setdefaulttimeout(5)
        my_addr = socket.getaddrinfo(mydomain, None)
        c = ssl.create_default_context()
        s = c.wrap_socket(socket.socket(), server_hostname=mydomain)
        s.connect((mydomain, 443))
        my_cert = s.getpeercert()
        get_my_cert_dated(mydomain, my_cert, my_addr)
    except ssl.CertificateError and socket.gaierror as e:
        pass


def get_my_cert_dated(domain, certs, my_addr):
    cert_beginning_time = parser.parse(certs['notBefore']).astimezone(pytz.utc)
    cert_end_time = parser.parse(certs['notAfter']).astimezone(pytz.utc)

    print('域名: %s  证书失效时间: %s' % (domain,  cert_end_time))


def read_domain_files():
    with open('G:\GitHub\learn\python學習\獲取SSL\domain.txt', 'r',
              encoding="utf-8") as file:
        for domain in file:
            try:
                get_my_domain(domain.strip())
            except Exception as e:
                print('域名: (%s)-%s' % (domain.strip(), e))


if __name__ == "__main__":
    read_domain_files()
