# -*- coding: UTF-8 -*-
import random
import string
from random import choice
import subprocess
import os
import re
import time
import xml.etree.cElementTree as ET

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

  # 點擊畫面座標


# ======================
class Element(object):
    """
    通過元素定位,需要Android 4.0以上
    """

    def __init__(self):
        """
        初始化，獲取系統臨時文件存儲目錄，定義匹配數字模式
        """
        self.tempFile = path
        self.pattern = re.compile(r"\d+")

    def __uidump(self):
        """
        獲取當前Activity控件樹
        """
        adb(f"adb -s {device_name} shell uiautomator dump /data/local/tmp/uidump.xml")
        time.sleep(0.5)
        adb(f"adb -s {device_name} pull /data/local/tmp/uidump.xml " + self.tempFile)
        time.sleep(0.5)

    def __element(self, attrib, name):
        """
        同屬性單個元素，返回單個座標元組
        """
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "\\uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])

                return Xpoint, Ypoint

    def __elements(self, attrib, name):
        """
        同屬性多個元素，返回座標元組列表
        """
        list = []
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "\\uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                list.append((Xpoint, Ypoint))
        return list

    def findElementByName(self, name):
        """
        通過元素名稱定位
        usage: findElementByName(u"設置")
        """
        return self.__element("text", name)

    def findElementsByName(self, name):
        return self.__elements("text", name)

    def findElementByClass(self, className):
        """
        通過元素類名定位
        usage: findElementByClass("android.widget.TextView")
        """
        return self.__element("class", className)

    def findElementsByClass(self, className):
        return self.__elements("class", className)

    def findElementById(self, id):
        """
        通過元素的resource-id定位
        usage: findElementsById("com.android.deskclock:id/imageview")
        """
        return self.__element("resource-id", id)

    def findElementsById(self, id):
        return self.__elements("resource-id", id)


class Event(object):
    def __init__(self):
        adb(f"adb -s {device_name} wait-for-device")

    def setting_master(self):
        adb(f"adb -s {device_name} shell am start com.android.settings/com.android.settings.Settings")

    def touch(self, dx, dy):
        """
        觸摸事件
        usage: touch(500, 500)
        """
        adb(f"adb -s {device_name} shell input tap " + str(dx) + " " + str(dy))
        # time.sleep(0.5)

    def swipe(self, dx, dy):
        # 滑動
        adb(f"adb -s {device_name} shell input swipe " + str(dx) +
            " " + str(dy) + " "+str(dx) + " " + str(dy-800))

    # 輸入文字
    def text(self, text):
        adb(f"adb -s {device_name} shell input text '{text}'")


# ===================
if __name__ == "__main__":
    # device_name = '149dc516'
    device_name = 'dc1b8102'
    # setting_google()
    # d = Device(device_name)
    element = Element()
    evevt = Event()
    # 開啟設置
    # evevt.setting_master()
    # # 找到google
    # for a in range(1, 5):
    #     try:
    #         e1 = element.findElementByName(u"Google")
    #         if e1 != 'None':
    #             evevt.touch(e1[0], e1[1])
    #             break
    #     except TypeError:
    #         evevt.swipe(290.0, 1709.5)
    # # 點擊管理您的 Google 帳戶
    # a = element.findElementByName(u"管理您的 Google 帳戶")
    # evevt.touch(a[0], a[1])

    # # 換帳號
    # a = element.findElementsById("com.google.android.gms:id/account")[0]
    # evevt.touch(a[0], a[1])

    # # # 新增帳號
    # a = element.findElementByName(u"新增其他帳號")
    # evevt.touch(a[0], a[1])

    # 選建立帳號
    # a = element.findElementByName(u"建立帳戶")
    # print(a)
    # evevt.touch(a[0], a[1])

    # # 選建立個人帳號
    # a = element.findElementByName(u"建立個人帳戶")
    # evevt.touch(a[0], a[1])

    # 輸入姓
    a = element.findElementById(u"lastName")
    evevt.touch(a[0], a[1])

    # 定義姓氏
    first_name = random.choice(first_name_list)
    print(first_name)
    evevt.text(first_name)

    # 輸入名
    a = element.findElementById(u"firstName")
    evevt.touch(a[0], a[1])

    second_name = str(random.choice(second_name_list) +
                      random.choice(second_name_list))
    evevt.text(second_name)

    print('名子: '+first_name+second_name)

    # 繼續
    a = element.findElementByName(u"繼續")
    evevt.touch(a[0], a[1])

    # 基本資訊
    a = element.findElementById(u"year")
    evevt.touch(a[0], a[1])
    year = str(random.randint(1990, 2009))
    evevt.text(year)
    print('年:'+year)

    a = element.findElementById(u"month")
    evevt.touch(a[0], a[1])

    month = str(random.randint(1, 12))
    a = element.findElementByName(f"{month} 月")
    evevt.touch(a[0], a[1])

    a = element.findElementById(u"day")
    evevt.touch(a[0], a[1])
    day = str(random.randint(1, 28))
    evevt.text(day)

    print('年:'+year, '月:'+month, '日:'+day)

    a = element.findElementByName(u"性別")
    evevt.touch(a[0], a[1])

    a = element.findElementByName(u"不願透露")
    evevt.touch(a[0], a[1])

    # 繼續
    a = element.findElementByName(u"繼續")
    evevt.touch(a[0], a[1])

    # 自行建立 Gmail 地址
    a = element.findElementByName(u"自行建立 Gmail 地址")
    evevt.touch(a[0], a[1])

    evevt.touch(217, 1162)

    # 輸入電子郵件
    # 生產隨季英文大小寫當帳號
    length_of_string = 9
    account = str(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length_of_string)))

    evevt.text(account)
    print('帳號: '+account)

    # 點繼續
    a = element.findElementByName(u"繼續")
    evevt.touch(a[0], a[1])

    # 點及密碼
    a = element.findElementByClass(u'android.widget.EditText')
    evevt.touch(a[0], a[1])

    # 生成密碼
    password = str(''.join([choice(
        string.ascii_letters + string.digits + string.punctuation) for i in range(12)]))

    evevt.text(password)
    print('密碼: '+password)

    # 點繼續
    a = element.findElementByName(u"繼續")
    evevt.touch(a[0], a[1])

    # 略過
    a = element.findElementByName(u"略過")
    evevt.touch(a[0], a[1])

    # 點繼續
    a = element.findElementByName(u"繼續")
    evevt.touch(a[0], a[1])

    # 點我同意
    a = element.findElementByName(u"我同意")
    evevt.touch(a[0], a[1])
