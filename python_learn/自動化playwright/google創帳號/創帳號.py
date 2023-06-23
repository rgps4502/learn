
import sys
from playwright.sync_api import Playwright, sync_playwright
import string
import time
import random
import os
import requests
import re
import pandas as pd
from datetime import date
session = requests.Session()
path = os.path.abspath(os.path.dirname(__file__))

# 姓氏字典
first_name_list = ['陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '洪', '郭', '邱', '曾', '廖', '賴', '徐', '周', '葉', '蘇', '莊', '呂', '江', '何', '蕭', '羅', '高', '潘', '簡', '朱', '鍾', '游', '彭', '詹', '胡', '施', '沈', '余', '盧', '梁', '趙', '顏', '柯', '翁', '魏', '孫',
                   '戴', '范', '方', '宋', '鄧', '杜', '傅', '侯', '曹', '薛', '丁', '卓', '阮', '馬', '董', '温', '唐', '藍', '石', '蔣', '古', '紀', '姚', '連', '馮', '歐', '程', '湯', '黄', '田', '康', '姜', '白', '汪', '鄒', '尤', '巫', '鐘', '黎', '涂', '龔', '嚴', '韓', '袁', '金', '童', '陸', '夏', '柳', '凃', '邵']
# 名字典
second_name_list = ['丹', '浩', '然', '婷', '建', '萍', '梓', '濤', '波', '敏', '麗', '桂', '詩', '華', '宣', '玉', '穎', '芳', '雪', '蘭', '珍', '勇', '雨', '強', '國', '偉', '靜', '燕', '霞', '俊', '杰', '軒', '諾',
                    '艷', '超', '豪', '平', '梅', '明', '佳', '宇', '秀', '斌', '子', '軍', '娟', '志', '紫', '杰', '怡', '鵬', '倩', '磊', '浩', '欣', '然', '皓', '涵', '紅', '徳', '悅', '一', '航', '鳳', '鑫', '帥', '俊', '和', '英']

heards = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def run(playwright: Playwright) -> None:
    # PC模式
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(locale="en-CN")
    # 手機模式
    # webkit = playwright.webkit
    # iphone = playwright.devices["iPhone 12 Pro"]
    # browser = webkit.launch(headless=False)
    # context = browser.new_context(**iphone)
    # Open new page
    page = context.new_page()

    # 開啟創帳號網頁
    page.goto("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=SignUp&hl=zh-TW")

    # Click text=繁體中文 >> nth=1
    # with page.expect_navigation(url="https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&hl=zh-TW&dsh=S845553%3A1659261640111543&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"):

    # Click [aria-label="姓氏"]
    page.locator("[aria-label=\"姓氏\"]").click()

    # 定義姓氏
    first_name = str(random.choice(first_name_list))
    # print('姓氏: ' + first_name)
    page.locator("[aria-label=\"姓氏\"]").fill(first_name)

    # Press Tab
    page.locator("[aria-label=\"姓氏\"]").press("Tab")

    second_name = str(random.choice(second_name_list) +
                      random.choice(second_name_list))

    print('名子: '+first_name+second_name)
    # Fill [aria-label="名字"]
    page.locator("[aria-label=\"名字\"]").fill(second_name)

    # Click [aria-label="使用者名稱"]
    page.locator("[aria-label=\"使用者名稱\"]").click()

    # 生產隨季英文大小寫當帳號
    length_of_string = 9
    account = str(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length_of_string)))

    print('帳號: '+account)

    # Fill [aria-label="使用者名稱"]
    page.locator("[aria-label=\"使用者名稱\"]").fill(account)

    # Click [aria-label="密碼"]
    page.locator("[aria-label=\"密碼\"]").click()

    # 生成密碼
    password = str(''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(11)))
    print('密碼: '+password)

    # Fill [aria-label="密碼"]
    page.locator("[aria-label=\"密碼\"]").fill(password)

    # Click [aria-label="確認"]
    page.locator("[aria-label=\"確認\"]").click()

    # Fill [aria-label="確認"]
    page.locator("[aria-label=\"確認\"]").fill(password)

    # Click button:has-text("繼續")

    # with page.expect_navigation():
    page.locator("button:has-text(\"繼續\")").click()
    try:
        check = page.locator(
            'text=目前無法建立 Google 帳戶，請稍後再試。').text_content()
        print(check)
        if check == '目前無法建立 Google 帳戶，請稍後再試。':
            print('創帳號過於頻繁請等五分鐘')
            # sys.exit(1)
    except Exception:
        pass

        # Click input[type="tel"]
    page.locator("input[type=\"tel\"]").click()

    # Click text=+886台灣 (+886)
    # page.locator("text=+886台灣 (+886)").click()
    # Click text=香港 (+852)
    # page.locator("text=香港 (+852)").click()
    while True:
        # 獲取電話號碼
        res = get_phone()

        phone_number = res['number']
        page.wait_for_timeout(0.7)
        print('手機號碼:', phone_number)
        # Fill input[type="tel"]
        page.locator("input[type=\"tel\"]").fill('+852'+phone_number)

        # Click button:has-text("繼續")
        # with page.expect_navigation():
        page.locator(
            '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

        # Click text=這組電話號碼無法用於驗證身分。
        page.wait_for_timeout(1.5)
        check = page.is_visible(
            '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div[2]/div[2]/div', timeout=2)
        print(check)

    # 獲取驗證碼
        orderID = res['orderid']
        print(orderID)
        if check == False:
            break
        else:
            page.locator("input[type=\"tel\"]").fill('')
            # 釋放手機號
            release_phone_number(orderID)

    code = get_phone_message(orderID)
    print('獲取到的驗證碼:', code)

    # Fill [aria-label="輸入驗證碼"]
    page.locator("[aria-label=\"輸入驗證碼\"]").fill(code)

    # Click button:has-text("驗證")

    with page.expect_navigation():
        page.locator("button:has-text(\"驗證\")").click()

    # 釋放手機號
    release_phone_number(orderID)

    # Click [aria-label="備援電子郵件地址 \(選填\)"]
    page.locator("[aria-label=\"備援電子郵件地址 \\(選填\\)\"]").click()
    bak_account = str(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length_of_string))+'@proton.me')
    page.locator(
        "[aria-label=\"備援電子郵件地址 \\(選填\\)\"]").fill(bak_account)
    print('備用信箱:', bak_account)
    # Click [aria-label="年"]
    page.locator("[aria-label=\"年\"]").click()

    # Fill [aria-label="年"]
    year = str(random.randint(1998, 2008))
    page.locator("[aria-label=\"年\"]").fill(year)

    month = str(random.randint(1, 12))
    # Select 7
    page.locator(
        "text=月1 月2 月3 月4 月5 月6 月7 月8 月9 月10 月11 月12 月 >> select").select_option(month)

    # Click [aria-label="日"]
    page.locator("[aria-label=\"日\"]").click()

    # Fill [aria-label="日"]
    day = str(random.randint(1, 28))
    page.locator("[aria-label=\"日\"]").fill(day)

    ymd = ('年:'+str(year) + ' 月:'+str(month) + ' 日:'+str(day))
    print('年:'+year, '月:'+month, '日:'+day)

    # Select 3
    page.locator("text=性別女性男性不願透露自訂 >> select").select_option("3")

    # Click button:has-text("繼續")

    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()

    # Click button:has-text("略過")

    with page.expect_navigation():
        page.locator("button:has-text(\"略過\")").click()

    # Click button:has-text("我同意")

    # 移除電話
    with page.expect_navigation():
        page.locator("button:has-text(\"我同意\")").click()

    page.goto('https://myaccount.google.com/security?hl=zh_TW')

    with page.expect_navigation():
        page.locator("[aria-label=\"備援電話號碼\"] >> text=備援電話號碼").click()

    # Click [aria-label="輸入您的密碼"]
    # page.locator("[aria-label=\"輸入您的密碼\"]").click(button="right")
    # Fill [aria-label="輸入您的密碼"]
    page.locator("[aria-label=\"輸入您的密碼\"]").fill(password)

    # Click button:has-text("繼續")
    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()
    # Click [aria-label="移除電話號碼"]
    page.locator("[aria-label=\"移除電話號碼\"]").click()

    with page.expect_navigation():
        page.locator(
            "div[role=\"button\"]:has-text(\"移除電話號碼\")").nth(1).click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

    # 寫入excel
    data = first_name+second_name, ymd, account, password, bak_account, '+852 '+phone_number
    excel(data)

# 獲取四方接口token


def get_token():
    params = {
        'name': 'pipi090301',
        'password': 'A1B2C3D4@@'
    }
    url = 'https://smsn.szfang.tw/api/login'
    headers = {
        'content-type': 'text/html; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['api_token']

# 獲取電話號碼


def get_phone():
    params = {
        'api_token': token,
        'projectId': 19
    }
    url = 'https://smsn.szfang.tw/api/getNumber'
    headers = {
        'content-type': 'text/html; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # 如果响应码不为 200，会抛出异常
        data = response.json()['data']
    except (requests.exceptions.RequestException, KeyError):
        print('獲取電話號碼失敗')
    finally:
        return data

    # 獲取驗證碼


def get_phone_message(orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/getSmsContent?'
    count = 0
    while count < 10:
        res = session.get(url, headers=heards, params=params).json()
        print(res)
        if res['msg'] == '正在获取驗證碼':
            time.sleep(2)
            count = count+1
            if count == 10:
                print('收不到驗證碼')
                # 釋放手機號
                release_phone_number(orderID)
                sys.exit(1)
        else:
            code = res['data']['messages']
            code = str([float(s)
                        for s in re.findall(r'\d+', code)][0]).strip(".0")
            break
    return code

# 釋放手機號


def release_phone_number(orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/releaseNumber?'
    res = session.get(url, headers=heards, params=params).json()
    print(res['msg'])


# 寫入excel
def excel(data):
    df = pd.DataFrame({
        "姓名": [data[0]],
        "生日": [data[1]],
        "帳號": [data[2]],
        "密碼": [data[3]],
        "備用信箱": [data[4]],
        "電話": [data[5]],
    })

    # print(df)
    today = date.today()
    excel_name = f'{path}\{today}.xlsx'

    # 檢查excel是否存在
    if os.path.isfile(excel_name):
        print("檔案存在。")
        old_data = pd.read_excel(excel_name)

        new_data = old_data.append({
            "姓名": data[0],
            "生日": data[1],
            "帳號": data[2],
            "密碼": data[3],
            "備用信箱": data[4],
            "電話": data[5]}, ignore_index=True)

        new_data.to_excel(excel_name, sheet_name="google帳號", index=False)
    else:
        print("檔案不存在寫入excle")
        df.to_excel(excel_name, sheet_name="google帳號", index=False)


if __name__ == '__main__':
    token = get_token()
    with sync_playwright() as playwright:
        run(playwright)
