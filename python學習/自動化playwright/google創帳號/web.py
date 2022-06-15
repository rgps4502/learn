import random
import string
from random import choice
from playwright.sync_api import Playwright, sync_playwright, expect

# 姓氏字典
first_name_list = ['陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '洪', '郭', '邱', '曾', '廖', '賴', '徐', '周', '葉', '蘇', '莊', '呂', '江', '何', '蕭', '羅', '高', '潘', '簡', '朱', '鍾', '游', '彭', '詹', '胡', '施', '沈', '余', '盧', '梁', '趙', '顏', '柯', '翁', '魏', '孫',
                   '戴', '范', '方', '宋', '鄧', '杜', '傅', '侯', '曹', '薛', '丁', '卓', '阮', '馬', '董', '温', '唐', '藍', '石', '蔣', '古', '紀', '姚', '連', '馮', '歐', '程', '湯', '黄', '田', '康', '姜', '白', '汪', '鄒', '尤', '巫', '鐘', '黎', '涂', '龔', '嚴', '韓', '袁', '金', '童', '陸', '夏', '柳', '凃', '邵']
# 名字典
second_name_list = ['丹', '浩', '然', '婷', '建', '萍', '梓', '濤', '波', '敏', '麗', '桂', '詩', '華', '宣', '玉', '穎', '芳', '雪', '蘭', '珍', '勇', '雨', '強', '國', '偉', '靜', '燕', '霞', '俊', '杰', '軒', '諾',
                    '艷', '超', '豪', '平', '梅', '明', '佳', '宇', '秀', '斌', '子', '軍', '娟', '志', '紫', '杰', '怡', '鵬', '倩', '磊', '浩', '欣', '然', '皓', '涵', '紅', '徳', '悅', '一', '航', '鳳', '鑫', '帥', '俊', '和', '英']


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # 開啟創帳號網頁
    page.goto("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com.tw%2F%3Fhl%3Dzh_TW&hl=zh-TW&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

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
    password = str(''.join([choice(
        string.ascii_letters + string.digits + string.punctuation) for i in range(12)]))
    print('密碼: '+password)

    # Fill [aria-label="密碼"]
    page.locator("[aria-label=\"密碼\"]").fill(password)

    # Click [aria-label="確認"]
    page.locator("[aria-label=\"確認\"]").click()

    # Fill [aria-label="確認"]
    page.locator("[aria-label=\"確認\"]").fill(password)

    # Click button:has-text("繼續")

    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()

    # Click input[type="tel"]
    page.locator("input[type=\"tel\"]").click()
    exit(1)
    # Fill input[type="tel"]
    page.locator("input[type=\"tel\"]").fill("0955556801")

    # Click button:has-text("繼續")

    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()

    # Fill [aria-label="輸入驗證碼"]
    page.locator("[aria-label=\"輸入驗證碼\"]").fill("204778")

    # Click button:has-text("驗證")

    with page.expect_navigation():
        page.locator("button:has-text(\"驗證\")").click()

    # Click [aria-label="備援電子郵件地址 \(選填\)"]
    page.locator("[aria-label=\"備援電子郵件地址 \\(選填\\)\"]").click()

    # Click [aria-label="年"]
    page.locator("[aria-label=\"年\"]").click()

    # Fill [aria-label="年"]
    page.locator("[aria-label=\"年\"]").fill("1994")

    # Select 7
    page.locator(
        "text=月1 月2 月3 月4 月5 月6 月7 月8 月9 月10 月11 月12 月 >> select").select_option("7")

    # Click [aria-label="日"]
    page.locator("[aria-label=\"日\"]").click()

    # Fill [aria-label="日"]
    page.locator("[aria-label=\"日\"]").fill("27")

    # Select 3
    page.locator("text=性別女性男性不願透露自訂 >> select").select_option("3")

    # Click button:has-text("繼續")

    with page.expect_navigation():
        page.locator("button:has-text(\"繼續\")").click()

    # Click button:has-text("略過")

    with page.expect_navigation():
        page.locator("button:has-text(\"略過\")").click()

    # Click button:has-text("我同意")

    with page.expect_navigation():
        page.locator("button:has-text(\"我同意\")").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':

    with sync_playwright() as playwright:
        run(playwright)
