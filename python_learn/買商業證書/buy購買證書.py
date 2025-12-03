# 登入cheapss

import requests
import time
from bs4 import BeautifulSoup
# 買證書URL
buy_url = 'https://cheapsslsecurity.com/comodo/positivessl-wildcard.html'


def req(session, url, header, payload=None):
    # 如果payload參數沒有給就當作是get請求否則為post請求
    if payload == 'None':
        r = session.get(url, headers=header, timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    else:
        r = session.post(url, headers=header, data=payload,
                         timeout=30)  # 獲取網頁30秒為限
        r.raise_for_status()  # 如果狀態不是200引發HTTPERROR異常
        r.encoding = r.apparent_encoding  # 用預測的解碼
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup


def get_http(url):

    header = {
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 登入用的data
    login_payload = {
        'referer': 'https://cheapsslsecurity.com/quicklogin.html?isauth=false&ReturnUrl=%2fclient%2fordersummary.html',
        '__VIEWSTATE': '/wEPDwUKMTY0Nzg0NzU0N2RkcweFlpgG3cvff6LrQyzoJkQhxetcYszKQQlHepcyA3c=',
        'ctl00$RapidSSLContent$txtUsername': 'email_account',
        'ctl00$RapidSSLContent$txtPassword': 'password',
        'ctl00$RapidSSLContent$btnLogin': 'Login',
        '__VIEWSTATEGENERATOR': '5F89FC59',
        '__EVENTVALIDATION': '/wEdAAQjkL3jJcqYFrkHnvBRdsxAcO1dB7UA/''GyDQStrVSOCjHfNGizx3lC8jGKGqxi1PhAlY6eIPpktbY3NBsQ56uSJzyNWoPoZW2Kb0YAmoEVdDHE07pO3YOp2SYd5w0n6Nxk=',
    }
    # 選擇購買1年的data
    data_page1 = {
        '__VIEWSTATE': '/wEPDwUKMTMzNjg1MTc1NQ8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgJmD2QWAgICD2QWAgIED2QWAgIBDw8WAh4KUHJvZHVjdFJvdzKiCgABAAAA/////wEAAAAAAAAADAIAAAA9U1NMREFMLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAUBAAAAEVNTTERBTC5Qcm9kdWN0Um93HwAAABpQcm9kdWN0Um93X0Jhc2UrX3Byb2R1Y3RJRBxQcm9kdWN0Um93X0Jhc2UrX3Byb2R1Y3ROYW1lI1Byb2R1Y3RSb3dfQmFzZStfcHJvZHVjdERlc2NyaXB0aW9uJFByb2R1Y3RSb3dfQmFzZStfZ2VvVHJ1c3RQcm9kdWN0Q29kZR5Qcm9kdWN0Um93X0Jhc2UrX2NhbmJlUmVpc3N1ZWQiUHJvZHVjdFJvd19CYXNlK19jYW5iZVJlaXNzdWVkTnVsbBxQcm9kdWN0Um93X0Jhc2UrX3JlaXNzdWVEYXlzIFByb2R1Y3RSb3dfQmFzZStfcmVpc3N1ZURheXNOdWxsG1Byb2R1Y3RSb3dfQmFzZStfcmVmdW5kRGF5cxxQcm9kdWN0Um93X0Jhc2UrX3JlSXNzdWVUeXBlI1Byb2R1Y3RSb3dfQmFzZStfaXNTdXBwb3J0QXZhaWxhYmxlJ1Byb2R1Y3RSb3dfQmFzZStfaXNTdXBwb3J0QXZhaWxhYmxlTnVsbB1Qcm9kdWN0Um93X0Jhc2UrX3N1cHBvcnRQcmljZSJQcm9kdWN0Um93X0Jhc2UrX2lzV2lsZENhcmRQcm9kdWN0JlByb2R1Y3RSb3dfQmFzZStfaXNXaWxkQ2FyZFByb2R1Y3ROdWxsH1Byb2R1Y3RSb3dfQmFzZStfaXNEb21haW5WZXR0ZWQjUHJvZHVjdFJvd19CYXNlK19pc0RvbWFpblZldHRlZE51bGwZUHJvZHVjdFJvd19CYXNlK19pc0FjdGl2ZR1Qcm9kdWN0Um93X0Jhc2UrX2lzQWN0aXZlTnVsbBpQcm9kdWN0Um93X0Jhc2UrX2lzRGVsZXRlZB5Qcm9kdWN0Um93X0Jhc2UrX2lzRGVsZXRlZE51bGwcUHJvZHVjdFJvd19CYXNlK19pc1NhbkVuYWJsZSBQcm9kdWN0Um93X0Jhc2UrX2lzU2FuRW5hYmxlTnVsbBdQcm9kdWN0Um93X0Jhc2UrX3Nhbk1pbhtQcm9kdWN0Um93X0Jhc2UrX3Nhbk1pbk51bGwXUHJvZHVjdFJvd19CYXNlK19zYW5NYXgbUHJvZHVjdFJvd19CYXNlK19zYW5NYXhOdWxsGFByb2R1Y3RSb3dfQmFzZStfYnJhbmRJRBxQcm9kdWN0Um93X0Jhc2UrX2JyYW5kSUROdWxsLlByb2R1Y3RSb3dfQmFzZStfaXNDb21wZXRpdGl2ZVVwZ3JhZGVTdXBwb3J0ZWQfUHJvZHVjdFJvd19CYXNlK19hbGxvd1NhbkJ1bmRsZQABAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAQEIAQgIAQEFAQEBAQEBAQEBAQgBCAEIAQEBAgAAAC4AAAAGAwAAACdDb21vZG8gUG9zaXRpdmVTU0wgV2lsZGNhcmQgQ2VydGlmaWNhdGUGBAAAACBQb3NpdGl2ZVNTTCBXaWxkY2FyZCBDZXJ0aWZpY2F0ZQYFAAAAE3Bvc2l0aXZlc3Nsd2lsZGNhcmQBAAcAAAAADwAAAAEAAAABAAc0OS4wMDAwAQAAAAEAAAAAAAAAAAAAAAAAAAAFAAAAAAAAC2QWAgIFDxYCHgtfIUl0ZW1Db3VudAIFFgwCAQ9kFgRmDxUJCXJidFByaWNlMAAENDcxNyExfDY3Ljk1fDI0OS4wMHw3MyV8MC4wMDAwfDY3Ljk1MDAACXJidFByaWNlMAExAyQ2NwI5NWQCAQ8WAh4Fc3R5bGUFDGRpc3BsYXk6bm9uZWQCAg9kFgRmDxUJCXJidFByaWNlMQAENDcxOCIyfDU3Ljk1fDQ1OC4wMHw3NSV8MC4wMDAwfDExNS45MDAwAAlyYnRQcmljZTEBMgMkNTcCOTVkAgEPFgIfAwUMZGlzcGxheTpub25lZAIDD2QWBGYPFQkJcmJ0UHJpY2UyAAQ0NzE5IjN8NTYuOTV8NzQ3LjAwfDc3JXwwLjAwMDB8MTcwLjg1MDAACXJidFByaWNlMgEzAyQ1NgI5NWQCAQ8WAh8DBQxkaXNwbGF5Om5vbmVkAgQPZBYEZg8VCQlyYnRQcmljZTMABDQ3MjAiNHw1NC45NXw5OTYuMDB8NzglfDAuMDAwMHwyMTkuODAwMAAJcmJ0UHJpY2UzATQDJDU0Ajk1ZAIBDxYCHwMFDGRpc3BsYXk6bm9uZWQCBQ9kFgRmDxUJCXJidFByaWNlNBFjaGVja2VkPSJjaGVja2VkIgQ1MTMxIjV8NTIuOTV8OTc2LjA4fDczJXwwLjAwMDB8MjY0Ljc1MDAwPHNwYW4gY2xhc3M9J2hpZGVtZSc+JDxzcGFuPiQ1Mi45NTwvc3Bhbj48L3NwYW4+CXJidFByaWNlNAE1AyQ1MgI5NWQCAQ8WAh8DZWQCBg9kFgRmDxUBAGQCAQ8VAQBkZGhM6okFbIK8O53D4GGd3X4G19hKPGRXmkxVXWQVnx/1',
        'ctl00$RapidSSLContent$uclPriceList1$drpQty': '1',
        'ctl00$RapidSSLContent$uclPriceList1$ibtnOrder': 'Add to Cart',
        'pricing': '4717',
        '__VIEWSTATEGENERATOR': 'CD95DC81',
        '__EVENTVALIDATION': '/wEdAAPBmLgCHxeYYPWBoXZuGWKPOXG5j/OXk/Abk9DvdET73xcraHeHgnMCsU9CISp91T5nROHSmNTUuqZQR15673B1kbwx+uiQET5cTTsfncwJGw=='
    }

    try:
        session = requests.session()
        # 登入
        soup = req(session, url, header, login_payload)
        # with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\login.html', 'w', encoding="utf-8") as f:
        #     f.write(str(soup))
        # # # 選擇一年
        # soup = req(
        #     session, 'https://cheapsslsecurity.com/comodo/positivessl-wildcard.aspx', header, data_page1)

        # # with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\body.html', 'w', encoding="utf-8") as f:
        # #     f.write(str(soup))
        # # 獲取post所需data的value 'ddlCountry': '202', 這202是對應選擇PH的代號
        # VIEWSTATE = soup.find(id="__VIEWSTATE")["value"]
        # EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")["value"]
        # VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")["value"]
        # txtEmailAddress = soup.find(id="txtEmailAddress")["value"]
        # hdnAvailabelCredit = soup.find(id="hdnAvailabelCredit")["value"]
        # hdnFinalAmount = soup.find(id="hdnFinalAmount")["value"]
        # txtFullName = soup.find(id="txtFullName")["value"]
        # txtCompanyName = soup.find(id="txtCompanyName")["value"]
        # txtAddress1 = soup.find(id="txtAddress1")["value"]
        # txtCity = soup.find(id="txtCity")["value"]
        # txtState = soup.find(id="txtState")["value"]
        # txtZip = soup.find(id="txtZip")["value"]
        # txtPhone = soup.find(id="txtPhone")["value"]
        # # # 確認帳戶金額頁面的data
        # data_page2 = {
        #     '__EVENTTARGET': '',
        #     '__EVENTARGUMENT': '',
        #     '__LASTFOCUS': '',
        #     '__VIEWSTATE': VIEWSTATE,
        #     'hdnIsAuthenticated': 'true',
        #     'hdnAvailabelCredit': hdnAvailabelCredit,
        #     'hdnFinalAmount': hdnFinalAmount,
        #     'hdnPaymentMethod': '0',
        #     'hdnLoginClick': "__doPostBack('lnkButton','')",
        #     'hdnPlaceOrderClick': "__doPostBack('lnkPlaceOrder','')",
        #     'hdnlnkUpdateCart': "__doPostBack('lnkUpdateCart','')",
        #     'hdnRefereshClick': "__doPostBack('lnkReferesh','')",
        #     'hdnPRole': 'False',
        #     'txtPassword': '',
        #     'txtEmailAddress': txtEmailAddress,
        #     'txtFullName': txtFullName,
        #     'txtCompanyName': txtCompanyName,
        #     'txtVATNumber': '',
        #     'ddlCountry': '202',
        #     'txtAddress1': txtAddress1,
        #     'txtCity': txtCity,
        #     'ddlState': '0',
        #     'txtState': txtState,
        #     'txtZip': txtZip,
        #     'txtPhone': txtPhone,
        #     'txtPhoneExt': '',
        #     'lnkPlaceOrder': 'Place Order',
        #     '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        #     '__EVENTVALIDATION': EVENTVALIDATION}

        # # 確認購買數量的頁面
        # soup = req(
        #     session, 'https://cheapsslsecurity.com/checkout.html?o=pwc', header, data_page2)
        # # with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\body2.html', 'w', encoding="utf-8") as f:
        # #     f.write(str(soup))

        # # 獲取確認所需data
        # VIEWSTATE = soup.find(id="__VIEWSTATE")["value"]
        # VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")["value"]
        # EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")["value"]

        # data_page3 = {
        #     '__VIEWSTATE': VIEWSTATE,
        #     'lnkPlaceOrder': 'Complete Order',
        #     '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
        #     '__EVENTVALIDATION': EVENTVALIDATION}

        # # 確認完成購買送出
        # soup = req(session, 'https://cheapsslsecurity.com/confirmation.html',
        #            header, data_page3)
        # with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\body3.html', 'w', encoding="utf-8") as f:
        #     f.write(str(soup))

        # 進入綁定donmain配置

        # 獲取創建的URL
        # create_url = 'https://cheapsslsecurity.com' + \
        #     soup.find(id='ucCheckoutOrders1_rptOrders_hrefCompleteOrder_0')[
        #         'href']
        create_url = 'https://cheapsslsecurity.com/client/entercsr.html?id=4717&ProductID=46&crid=6680450'

        # 獲取選擇的data
        soup = req(
            session, create_url, header)
        VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
        VIEWSTATEGENERATOR = soup.find(id='__VIEWSTATEGENERATOR')['value']
        EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')['value']

        # 選擇配置證書頁面1的data
        ssl_config_data = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': VIEWSTATE,
            'ctl00$RapidSSLContent$ctl00$OrderType': 'rbtNewOrder',
            'ctl00$RapidSSLContent$ctl00$Warranty': 'rbt50kWarranty',
            'ctl00$RapidSSLContent$ctl00$SiteSeal': 'rbtPositiveSiteSeal',
            'ctl00$RapidSSLContent$ctl00$btnSubmit': 'Continue',
            'hdnproductName': 'PositiveSSL Wildcard Certificate',
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__SCROLLPOSITIONX': '0',
            '__SCROLLPOSITIONY': '1210',
            '__EVENTVALIDATION': EVENTVALIDATION
        }
        # 確認ssl第一頁配置
        soup = req(session, create_url, header, ssl_config_data)

        with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\ssl_config.html', 'w', encoding="utf-8") as f:
            with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\kf8544.com.csr', 'r', encoding="utf-8") as re:
                f.write(str(soup))
                CSR = re.read()
        # 獲取ssl ENTER CSR配置所需data
        VIEWSTATE = soup.find(id='__VIEWSTATE')['value']
        VIEWSTATEGENERATOR = soup.find(id='__VIEWSTATEGENERATOR')['value']
        EVENTVALIDATION = soup.find(id='__EVENTVALIDATION')['value']
        ssl_config_data2 = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': VIEWSTATE,
            'ctl00$RapidSSLContent$ctl00$DVAuth': 'rbtCNAMEAuth',
            'ctl00$RapidSSLContent$ctl00$txtCSR': CSR,
            'ctl00$RapidSSLContent$ctl00$drpWebserver': '36',
            'ctl00$RapidSSLContent$ctl00$btnSubmit': 'Continue',
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            '__SCROLLPOSITIONX': '0',
            '__SCROLLPOSITIONY': '1915',
            '__EVENTVALIDATION': EVENTVALIDATION
        }
        # 確認ssl ENTER CSR配置
        soup = req(session, 'https://cheapsslsecurity.com/client/entercsr.html',
                   header, ssl_config_data2)

        with open('G:\\GitHub\\learn\\python 學習\\買商業證書\\ssl_config2.html', 'w', encoding="utf-8") as f:
            f.write(str(soup))

        #獲取SSL VERIFY YOUR URL頁配置


    except Exception as e:
        print(e)


url = 'https://cheapsslsecurity.com/quicklogin.aspx?isauth=false&ReturnUrl=%2fclient%2fordersummary.html'
get_http(url)
