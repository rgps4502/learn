from urllib.request import ssl, socket
from datetime import datetime
import pandas as pd
import json

# @title 獲取網站 SSL 憑證
# url = 'expired.badssl.com'   #80  @param {type: "string"}
url = 'myself-bbs.com'  # 443
context = ssl.create_default_context()
try:
    with socket.create_connection((url, '443')) as sock:
        with context.wrap_socket(sock, server_hostname=url) as ssock:
            ver = ssock.version()
            data = ssock.getpeercert()

    print('TLS 的版本為：', ver, '\n')
    print('SSL 憑證的細節為：')
    print(data)
except ssl.SSLCertVerificationError as err:
    print(str(err))
    print(str(err).split('certificate verify failed: ')[1])
except Exception as err:
    print(str(err))
