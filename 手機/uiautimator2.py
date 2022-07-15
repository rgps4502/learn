# -*- coding: UTF-8 -*-
import random
import string
import time
from sqlalchemy import true
import uiautomator2 as u2
from random import choice
import subprocess
import os
import pandas as pd
from datetime import date


path = os.path.abspath(os.path.dirname(__file__))

# 姓氏字典
first_name_list = ['陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '洪', '郭', '邱', '曾', '廖', '賴', '徐', '周', '葉', '蘇', '莊', '呂', '江', '何', '蕭', '羅', '高', '潘', '簡', '朱', '鍾', '游', '彭', '詹', '胡', '施', '沈', '余', '盧', '梁', '趙', '顏', '柯', '翁', '魏', '孫',
                   '戴', '范', '方', '宋', '鄧', '杜', '傅', '侯', '曹', '薛', '丁', '卓', '阮', '馬', '董', '温', '唐', '藍', '石', '蔣', '古', '紀', '姚', '連', '馮', '歐', '程', '湯', '黄', '田', '康', '姜', '白', '汪', '鄒', '尤', '巫', '鐘', '黎', '涂', '龔', '嚴', '韓', '袁', '金', '童', '陸', '夏', '柳', '凃', '邵']
# 名字典
second_name_list = ['丹', '浩', '然', '婷', '建', '萍', '梓', '濤', '波', '敏', '麗', '桂', '詩', '華', '宣', '玉', '穎', '芳', '雪', '蘭', '珍', '勇', '雨', '強', '國', '偉', '靜', '燕', '霞', '俊', '杰', '軒', '諾',
                    '艷', '超', '豪', '平', '梅', '明', '佳', '宇', '秀', '斌', '子', '軍', '娟', '志', '紫', '杰', '怡', '鵬', '倩', '磊', '浩', '欣', '然', '皓', '涵', '紅', '徳', '悅', '一', '航', '鳳', '鑫', '帥', '俊', '和', '英']


# adb指令

def adb(command):
    proc = subprocess.Popen(command.split(
        ' '), stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    return out.decode('utf-8')

  # 點擊setting


def setting_master():
    adb(f"adb -s {device_name} shell am start com.android.settings/com.android.settings.Settings")


#
def create_google_account(d):

    d.healthcheck()
    # 進入設定
    setting_master()
    # print(d.device_info)
    # 找到google
    for a in range(1, 5):
        try:
            d(resourceId="android:id/title", text="Google").click(0.05)
            break
        except Exception:
            d.swipe_ext("up")
            time.sleep(0.5)

    # 點擊管理您的 Google 帳戶
    d(resourceId="com.google.android.gms:id/action_button").click()

    while true:
        # # 換帳號
        d.xpath(
            '//*[@resource-id="com.google.android.gms:id/account_spinner"]/android.widget.ImageView[1]').click()

        # 等待驗證等待120秒
        d.implicitly_wait(120.0)

        # 新增帳號
        d(resourceId="com.google.android.gms:id/add_account_chip_title").click()

        # 選建立帳號
        d(text="建立帳戶").click()

        # 選建立個人帳號
        d(text="建立個人帳戶").click()

        # 輸入姓
        d(resourceId="lastName").click()
        first_name = random.choice(first_name_list)
        d.send_keys(first_name, clear=True)

        # 定義名
        d(resourceId="firstName").click()
        second_name = str(random.choice(second_name_list) +
                          random.choice(second_name_list))
        d.send_keys(second_name, clear=True)

        print('名子: '+first_name+second_name)

        d(text="繼續").click()

        # 選擇年分
        d.xpath('//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]').click()
        year = str(random.randint(1998, 2008))
        d.send_keys(year, clear=True)

        # 月
        d.xpath(
            '//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[2]').click()
        month = str(random.randint(1, 12))
        d(resourceId="android:id/text1", text=f"{month} 月").click()

        # 日
        d.xpath('//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[3]/android.view.View[3]').click()
        day = str(random.randint(1, 28))
        d.send_keys(day, clear=True)
        ymd = ('年:'+str(year) + ' 月:'+str(month) + ' 日:'+str(day))
        print('年:'+year, '月:'+month, '日:'+day)

        # 性別
        d.xpath(
            '//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[4]').click()
        d(resourceId="android:id/text1", text="不願透露").click()
        # 繼續
        d(text="繼續").click()

        # 獲取帳號
        d.xpath('//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.RadioButton[1]').click()
        account = d.xpath(
            '//*[@resource-id="view_container"]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.RadioButton[1]').info['text']

        print(account)

        # 繼續
        d(text="繼續").click()

        # 生成密碼
        password = str(''.join([choice(
            string.ascii_letters + string.digits + string.punctuation) for i in range(12)]))
        d.xpath('//android.widget.EditText').click()
        d.send_keys(password, clear=True)
        print(password)

        # 繼續
        d(text="繼續").click()
        time.sleep(0.5)
        d.swipe_ext("up")

        d(text="略過").click()

        # 繼續
        d(text="繼續").click()

        for a in range(1, 5):
            try:
                d(text="我同意").click(0.05)
                break
            except Exception:
                d.swipe_ext("up")
                time.sleep(0.4)
        # 寫入excel
        data = first_name+second_name, ymd, account, password
        excel(data)

# def del_google_account(d):


def excel(data):
    df = pd.DataFrame({
        "姓名": [data[0]],
        "生日": [data[1]],
        "帳號": [data[2]],
        "密碼": [data[3]],
    })

    # print(df)
    today = date.today()
    excel_name = f'{path}\{today}.xlsx'

    # 檢查excel是否存在
    if os.path.isfile(excel_name):
        print("檔案存在。")
        data = pd.read_excel(excel_name)

        new_data = data.append({"姓名": data[0], "生日": data[1],
                                "帳號": data[2], "密碼": data[3]}, ignore_index=True)

        new_data.to_excel(excel_name, sheet_name="google帳號", index=False)
    else:
        print("檔案不存在寫入excle")
        df.to_excel(excel_name, sheet_name="google帳號", index=False)


# ===================
if __name__ == "__main__":
    # device_name = '149dc516'
    device_name = 'dc1b8102'
    d = u2.connect(device_name)
    # 創建google帳號
    google = create_google_account(d)
    # print(google)
    # 寫入excel

    # 從設備上移除帳號
    # del_google_account(d)
