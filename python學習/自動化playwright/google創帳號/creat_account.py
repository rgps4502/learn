from playwright.sync_api import Playwright, sync_playwright
import time
import sys
from 驗證email import verify_google
import random
import requests
import string

# 姓氏字典
first_name_list = ['陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '洪', '郭', '邱', '曾', '廖', '賴', '徐', '周', '葉', '蘇', '莊', '呂', '江', '何', '蕭', '羅', '高', '潘', '簡', '朱', '鍾', '游', '彭', '詹', '胡', '施', '沈', '余', '盧', '梁', '趙', '顏', '柯', '翁', '魏', '孫',
                   '戴', '范', '方', '宋', '鄧', '杜', '傅', '侯', '曹', '薛', '丁', '卓', '阮', '馬', '董', '温', '唐', '藍', '石', '蔣', '古', '紀', '姚', '連', '馮', '歐', '程', '湯', '黄', '田', '康', '姜', '白', '汪', '鄒', '尤', '巫', '鐘', '黎', '涂', '龔', '嚴', '韓', '袁', '金', '童', '陸', '夏', '柳', '凃', '邵']
# 名字典
second_name_list = ['丹', '浩', '然', '婷', '建', '萍', '梓', '濤', '波', '敏', '麗', '桂', '詩', '華', '宣', '玉', '穎', '芳', '雪', '蘭', '珍', '勇', '雨', '強', '國', '偉', '靜', '燕', '霞', '俊', '杰', '軒', '諾',
                    '艷', '超', '豪', '平', '梅', '明', '佳', '宇', '秀', '斌', '子', '軍', '娟', '志', '紫', '杰', '怡', '鵬', '倩', '磊', '浩', '欣', '然', '皓', '涵', '紅', '徳', '悅', '一', '航', '鳳', '鑫', '帥', '俊', '和', '英']


headers = {
    'content-type': 'text/html; charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 獲取四方token


def get_token():
    params = {
        'name': 'pipi090301',
        'password': 'A1B2C3D4@@'
    }
    url = 'https://smsn.szfang.tw/api/login'
    response = requests.get(url, headers=headers, params=params)
    return response.json()['api_token']


# 獲取電話
def get_phone_message(api_token):
    params = {
        'api_token': api_token,
        'projectId': 19
    }
    url = 'https://smsn.szfang.tw/api/getNumber'
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # 如果响应码不为 200，会抛出异常
        data = response.json()
    except (requests.exceptions.RequestException, KeyError):
        print('獲取電話號碼失敗')
    finally:
        return data


# 獲取電話號碼
def get_phone_number(token):
    phone_message = get_phone_message(api_token=token)
    if phone_message['msg'] == '獲取成功':
        phone_number = '+852'+phone_message['data']['number']
        orderid = phone_message['data']['orderid']
        print('獲取到號碼:', phone_message)
        return phone_number, orderid
    else:
        print('獲取號碼失敗', phone_message['msg'])
        sys.exit(1)


# 釋放手機號


def release_phone_number(token, orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/releaseNumber?'
    res = requests.get(url, headers=headers, params=params).json()
    print(res['msg'])


# 獲取驗證碼


def get_phone_code(token, orderID):
    params = {
        'api_token': token,
        'orderid': orderID
    }
    url = 'https://smsn.szfang.tw/api/getSmsContent?'
    count = 0
    while count < 10:
        res = requests.get(url, headers=headers, params=params).json()
        print(res)
        if res['msg'] == '正在获取驗證碼':
            time.sleep(2)
            count = count+1
            if count == 10:
                print('收不到驗證碼')
                # 釋放手機號
                release_phone_number(token, orderID)
                sys.exit(1)
        else:
            code = res['data']['messages'].split(' ')[0][2:]
            break
    return code


with sync_playwright() as playwright:
    # 设置浏览器选项
    server = '45.119.82.101:3333'
    browser = playwright.firefox.launch(headless=False, proxy={
        'server': f'http://{server}'})
    # browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(proxy={
        'server': f'http://{server}'})
    # context = browser.new_context()
    # 创建一个新的页面
    page = context.new_page()
    # 访问Google注册页面
    page.goto('https://accounts.google.com/signup/v2/webcreateaccount?hl=zh-TW&flowName=GlifWebSignIn&flowEntry=SignUp')
    # 等待注册表单出现
    page.wait_for_selector('#firstName')
    # 输入名字
    first_name = str(random.choice(first_name_list))
    page.fill('#firstName', first_name)
    second_name = str(random.choice(second_name_list) +
                      random.choice(second_name_list))
    # 输入姓氏
    page.fill('#lastName', second_name)
    print('名子: '+first_name+second_name)
    # 输入用户名
    # 生產隨季英文大小寫當帳號
    length_of_string = 9
    account = str(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length_of_string)))

    print('帳號: '+account)
    page.fill('#username', account)
    # 输入密码
    password = str(''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(11)))
    print('密碼: '+password)
    page.fill('input[name="Passwd"]', password)
    # 确认密码
    page.fill('input[name="ConfirmPasswd"]', password)
    # 点击下一步按钮
    page.click('#accountDetailsNext')
    # 等待创建账户完成
    page.wait_for_selector('#view_container')

    # 獲取號碼
    token = get_token()
    phone_number, orderid = get_phone_number(token)
    # 填写电话号码
    page.fill('#phoneNumberId', phone_number)
    # 点击下一步按钮
    with page.expect_navigation():
        page.get_by_role("button", name="繼續").click()

    code = get_phone_code(token, orderid)
    print('獲取到的驗證碼:', code)

    # Fill [aria-label="輸入驗證碼"]
    page.locator("[aria-label=\"輸入驗證碼\"]").fill(code)

    with page.expect_navigation():
        page.locator("button:has-text(\"驗證\")").click()

    # 釋放手機號
    release_phone_number(token, orderid)

    # Click [aria-label="備援電子郵件地址 \(選填\)"]
    page.locator("[aria-label=\"備援電子郵件地址 \\(選填\\)\"]").click()
    bak_account = str(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length_of_string))+'@yopmail.com')
    page.locator(
        "[aria-label=\"備援電子郵件地址 \\(選填\\)\"]").fill(bak_account)
    print('備用信箱:', bak_account)
    # Click [aria-label="年"]
    page.locator("[aria-label=\"年\"]").click()

    # Fill [aria-label="年"]
    year = str(random.randint(1988, 2005))
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

    # Select 1~3
    page.locator("text=性別女性男性不願透露自訂 >> select").select_option(
        str(random.randint(1, 3)))

    # Click button:has-text("繼續")

    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()

    # Click button:has-text("略過")

    with page.expect_navigation():
        page.locator("button:has-text(\"略過\")").click()

    with page.expect_navigation():
        page.get_by_role("button", name="我同意").click()

    with page.expect_navigation():
        page.get_by_role("link", name="Security", exact=True).click()

    with page.expect_navigation():
        page.get_by_role("link", name="Recovery phone").click()

    with page.expect_navigation():
        page.get_by_role("button", name="Remove phone number").click()

    with page.expect_navigation():
        page.get_by_role("button", name="Remove number").click()

    with page.expect_navigation():
        page.get_by_role("button", name="Back").click()

    with page.expect_navigation():
        page.get_by_role("link", name="Recovery email", exact=True).click()

    with page.expect_navigation():
        page.get_by_role("button", name="Next").click()

    # 獲取google驗證碼
    google_code = verify_google(bak_account)

    page.get_by_label("Verification code").click()
    page.get_by_label("Verification code").fill(google_code)
    time.sleep(3)
    page.get_by_role("button", name="Verify").click()

    time.sleep(2)
    with page.expect_navigation():
        page.get_by_role(
            "button", name=f"Google 帳戶： {first_name+second_name} ({account}@gmail.com)").click()

    with page.expect_navigation():
        page.frame_locator("iframe[name=\"account\"]").get_by_role(
            "link", name="登出").click()

    with page.expect_navigation():
        page.get_by_role("link", name="移除帳戶").click()

    with page.expect_navigation():
        page.get_by_role(
            "link", name=f"{first_name+second_name} {account}@gmail.com").click()

    with page.expect_navigation():
        page.get_by_role("button", name="是，我要移除").click()

    time.sleep(9999)
    # 创建账户完成后，做其他操作
    # ...
    # 关闭浏览器
    browser.close()
