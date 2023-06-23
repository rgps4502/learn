import os
from pandas import DataFrame
import io
import numpy as np
from PIL import Image
from playwright.sync_api import Playwright, sync_playwright, expect
from io import BytesIO
# 獲取腳本執行目錄
path = os.path.abspath(os.path.dirname(__file__))
# 截圖


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.boce.com/http
    page.goto("https://www.boce.com/http")

    # Click a:has-text("登录") >> nth=1
    with page.expect_popup() as popup_info:
        page.locator("a:has-text(\"登录\")").nth(1).click()
    page1 = popup_info.value

    # Click [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").click()

    # Fill [placeholder="密码"]
    page1.locator("[placeholder=\"密码\"]").fill("Gz39Yj8hfvCuUw2t")

    # Click [placeholder="手机号码\/邮箱地址"]
    page1.locator("[placeholder=\"手机号码\\/邮箱地址\"]").click(modifiers=["Meta"])

    # Fill [placeholder="手机号码\/邮箱地址"]
    page1.locator("[placeholder=\"手机号码\\/邮箱地址\"]").fill("13099438051")

    # Click button:has-text("登录")
    # with page1.expect_navigation(url="https://www.boce.com/user/#/dashboard"):
    with page1.expect_navigation():
        page1.locator("button:has-text(\"登录\")").click()

    # Close page
    page1.close()

    for domain in domains:
        # Click [placeholder="请输入有效的URL地址"]
        page.locator("[placeholder=\"请输入有效的URL地址\"]").click()

        # Fill [placeholder="请输入有效的URL地址"]
        page.locator("[placeholder=\"请输入有效的URL地址\"]").fill(str(domain))

        # Click text=检测一下
        # with page.expect_navigation(url="https://www.boce.com/http/918gg.vip"):
        with page.expect_navigation():
            page.locator("text=检测一下").click()

        # 等待text=已检测结束 視窗出現 等待50秒
        page.wait_for_selector("text=已检测结束", state='attached', timeout=50000)
        # page.locator("text=已检测结束").click()

        # # 截圖 Click canvas 下載
        element_handle = page.query_selector("//canvas")  # 按照元素截图

        # 儲存至list

        image = Image.open(io.BytesIO(element_handle.screenshot()))
        # 儲存至指定list中
        image_list.append(image)
        # 儲存至指定目錄
        # element_handle.screenshot(
        #     path=path+'\{0}.png'.format(domain))

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


# 圖片二維分析
def analyze_image(image):
    # 開啟圖片
    # image = Image.open(path+'\{0}.png'.format(image)).convert('RGB')
    image = image.convert('RGB')
    arr = np.asarray(image)
    newArr = arr.copy()

    red = np.array([224, 65, 76])
    cnt = 0

    white = np.array([255, 255, 255])
    wPoint = 0

    for x in newArr:
        for y in x:
            if (y == white).all():
                wPoint += 1
            elif (y == red).all():
                cnt += 1
                y[0], y[1], y[2] = 0, 0, 0

    # print(f' 異常佔比 {round(cnt/(arr.shape[0]*arr.shape[1]-wPoint), 3)}')
    result_list.append(round(cnt/(arr.shape[0]*arr.shape[1]-wPoint), 3))

    # newImg = Image.fromarray(newArr).convert('RGB')
    # biImg = newImg.convert("L")
    # biArr = np.asarray(biImg)
    # biArr = (biArr > 0) * 255
    # biImg = Image.fromarray(biArr).convert('RGB')

    # biImg.show()


def write_excel():

    data = {'域名': domains, '異常佔比': result_list}
    # 寫入資料
    df = DataFrame(data)
    # 以域名當地一列 不使用的話會出現0~索引流水號
    df.set_index('域名', inplace=True)
    # 檔案存放位置
    df.to_excel(path+'\data.xlsx', sheet_name='域名檢測')


domains = ["918gg.vip", "918ucc.com", "google.com"]
# domains = ["google.com"]
image_list = []
result_list = []
# 獲取圖片
with sync_playwright() as playwright:
    run(playwright)

# 圖片二維分析
# for domain in domains:
#     analyze_image(domain)

for image in image_list:
    analyze_image(image)

# 寫入excel
write_excel()
