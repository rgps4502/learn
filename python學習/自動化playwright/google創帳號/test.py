# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class Google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_google(self):
        driver = self.driver
        google = 1
        cont = 1
        while cont <= 10:
            if cont != 1:
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${google} | ]]
                driver.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=SignUp&hl=zh-TW")

            # ERROR: Caught exception [unknown command [pageWait]]
            driver.execute_script("document.myWindow=window.open(\"https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=SignUp&hl=zh-TW\")")
            sms = 2
            driver.execute_script(
                "document.myWindow=window.open(\"https://smsn.szfang.tw/smsList\")")
            # ERROR: Caught exception [unknown command [pageWait]]
            # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${google} | ]]
            # ERROR: Caught exception [unknown command [pageWait]]
            myArray = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(
                sms) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms }; return " + u"['王','李','張','劉','陳','楊','黃','趙','吳','周','徐','孫','馬','朱','胡','郭','何','高','林','鄭','謝','羅','梁','宋','唐','許','韓','馮','鄧','曹','彭','曾','蕭','田','董','袁','潘','於','蔣','蔡','余','杜','葉','程','蘇','魏','呂','丁','任','沈','姚','盧','姜','崔','鍾','譚','陸','汪','范','金','石','廖','賈','夏','韋','付','方','白','鄒','孟','熊','秦','邱','江','尹','薛','閆','段','雷','侯','龍','史','陶','黎','賀','顧','毛','郝','龔','邵','萬','錢','嚴','覃','武','戴','莫','孔','向','湯']")
            rand = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(
                myArray) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray }; return " + "~~(Math.random()*myArray.length)")
            fistname = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(
                myArray) + "\";var rand = \"" + str(rand) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand }; return " + "myArray[rand]")
            myArray2 = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(
                fistname) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname }; return " + u"['丹', '浩', '然', '婷', '建', '萍', '梓', '濤', '波', '敏', '麗', '桂', '詩', '華', '宣', '玉', '穎', '芳', '雪', '蘭', '珍', '勇', '雨', '強', '國', '偉', '靜', '燕', '霞', '俊', '杰', '軒', '諾','艷', '超', '豪', '平', '梅', '明', '佳', '宇', '秀', '斌', '子', '軍', '娟', '志', '紫', '杰', '怡', '鵬', '倩', '磊', '浩', '欣', '然', '皓', '涵', '紅', '徳', '悅', '一', '航', '鳳', '鑫', '帥', '俊', '和', '英','陳', '林', '黃', '張', '李', '王', '吳', '劉', '蔡', '楊', '許', '鄭', '謝', '洪', '郭', '邱', '曾', '廖', '賴', '徐', '周', '葉', '蘇', '莊', '呂', '江', '何', '蕭', '羅', '高', '潘', '簡', '朱', '鍾', '游', '彭', '詹', '胡', '施', '沈', '余', '盧', '梁', '趙', '顏', '柯', '翁', '魏', '孫','戴', '范', '方', '宋', '鄧', '杜', '傅', '侯', '曹', '薛', '丁', '卓', '阮', '馬', '董', '温', '唐', '藍', '石', '蔣', '古', '紀', '姚', '連', '馮', '歐', '程', '湯', '黄', '田', '康', '姜', '白', '汪', '鄒', '尤', '巫', '鐘', '黎', '涂', '龔', '嚴', '韓', '袁', '金', '童', '陸', '夏', '柳', '凃', '邵']")
            rand = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(
                fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2 }; return " + "~~(Math.random()*myArray2.length)")
            last1 = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(
                fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2 }; return " + "myArray2[rand]")
            rand = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(
                myArray2) + "\";var last1 = \"" + str(last1) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1 }; return " + "~~(Math.random()*myArray2.length)")
            last2 = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(
                myArray2) + "\";var last1 = \"" + str(last1) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1 }; return " + "myArray2[rand]")
            lastname = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(
                myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2 }; return " + "last1+last2")
            user = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(
                last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname }; return " + "fistname+last1+last2")
            driver.find_element_by_id("lastName").clear()
            driver.find_element_by_id("lastName").send_keys(fistname)
            driver.find_element_by_id("firstName").clear()
            driver.find_element_by_id("firstName").send_keys(lastname)
            time.sleep(1)
            account = driver.find_element_by_xpath(
                "//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button").text
            driver.find_element_by_xpath(
                "//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button").click()
            password = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(
                lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account }; return " + "Math.random().toString(36).substring(2,13)")
            driver.find_element_by_name("Passwd").clear()
            driver.find_element_by_name("Passwd").send_keys(password)
            driver.find_element_by_name("ConfirmPasswd").clear()
            driver.find_element_by_name("ConfirmPasswd").send_keys(password)
            driver.find_element_by_xpath(
                "//div[@id='accountDetailsNext']/div/button/span").click()
            time.sleep(1)
            是否需要輸入電話 = self.is_element_present(
                By.XPATH, "//*[(@id = \"gender\")]")
            if 是否需要輸入電話 == "false":
                # ERROR: Caught exception [unknown command [pageWait]]
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${sms} | ]]
                # ERROR: Caught exception [unknown command [pageWait]]
                帳號 = self.is_element_present(By.LINK_TEXT, u"還沒註冊?")
                if 帳號 == true:
                    driver.find_element_by_id("name").clear()
                    driver.find_element_by_id("name").send_keys("pipi090301")
                    driver.find_element_by_id("password").clear()
                    driver.find_element_by_id(
                        "password").send_keys("A1B2C3D4@@")
                    driver.find_element_by_xpath(
                        "//button[@type='submit']").click()

                errphone = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(
                    user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號 }; return " + "0")
                # ERROR: Caught exception [ERROR: Unsupported command [label | errorphone | ]]
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${sms} | ]]
                if (cont != 1 or errphone == 1):
                    driver.refresh()
                    errphone = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(
                        account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone }; return " + "0")

                driver.find_element_by_id("selectpro").click()
                # ERROR: Caught exception [unknown command [pageWait]]
                # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
                try:
                    self.assertEqual("off", driver.find_element_by_xpath(
                        "//table[@id='prolist']/tbody/tr[4]/td/input").get_attribute("value"))
                except AssertionError as e:
                    self.verificationErrors.append(str(e))
                driver.find_element_by_xpath(
                    "//table[@id='prolist']/tbody/tr[4]/td/input").click()
                # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
                try:
                    self.assertEqual("", driver.find_element_by_id(
                        "number").get_attribute("value"))
                except AssertionError as e:
                    self.verificationErrors.append(str(e))
                driver.find_element_by_id("selectnumnode").click()
                四方餘額 = self.is_element_present(
                    By.XPATH, "//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"layui-layer-content\", \" \" ))]")
                if 四方餘額 == true:
                    print(u"四方餘額不足請儲值")

                time.sleep(1)
                number = driver.find_element_by_id(
                    "number").get_attribute("value")
                number = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(
                    是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number }; return " + "\"+852 \"+" + str(number))
                number = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(
                    是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number }; return " + "number.toString()")
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${google} | ]]
                time.sleep(1)
                driver.find_element_by_id("phoneNumberId").click()
                driver.find_element_by_id("phoneNumberId").clear()
                driver.find_element_by_id("phoneNumberId").send_keys(number)
                driver.find_element_by_xpath(
                    "//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div/div/div/button/span").click()
                time.sleep(1)
                無法驗證號碼 = self.is_element_present(
                    By.XPATH, "//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"o6cuMc\", \" \" ))]")
                if 無法驗證號碼 == true:
                    無法使用電話 = driver.find_element_by_xpath(
                        "//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"o6cuMc\", \" \" ))]").text
                    # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent | 無法使用電話==這組電話號碼用過太多次 | ]]
                    # ERROR: Caught exception [unknown command [If]]
                    cont = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(
                        帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話 }; return " + str(errphone) + "+1")
                    # ERROR: Caught exception [ERROR: Unsupported command [gotoLabel | errorphone | ]]

                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${sms} | ]]
                driver.find_element_by_xpath(
                    "//*[(@id = \"deletebymber\")]").click()
                time.sleep(1)
                # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${google} | ]]
                time.sleep(9999999999.999)

            # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${sms} | ]]
            time.sleep(1)
            self.is_element_present(
                By.XPATH, u"(.//*[normalize-space(text()) and normalize-space(.)='內容'])[1]/following::td[3]")
            code = driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='內容'])[1]/following::td[3]").text
            code = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(
                errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code }; return " + "code.toString().substring(2, 8)")
            # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_${google} | ]]
            time.sleep(1)
            driver.find_element_by_id("code").click()
            driver.find_element_by_id("code").clear()
            driver.find_element_by_id("code").send_keys(code)
            driver.find_element_by_xpath(
                "//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"qIypjc\", \" \" ))]//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"VfPpkd-vQzf8d\", \" \" ))]").click()
            # ERROR: Caught exception [unknown command [endif]]
            myArray = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(
                number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code }; return " + "['@yopmail.fr','@yopmail.net','@cool.fr.nf','@jetable.fr.nf','@courriel.fr.nf','@moncourrier.fr.nf','@monemail.fr.nf','@monmail.fr.nf','@hide.biz.st','@mymail.infos.st']")
            rand = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(
                errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code }; return " + "~~(Math.random()*myArray.length)")
            rValue = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(
                errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code }; return " + "myArray[rand]")
            bak2 = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(
                四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var rValue = \"" + str(rValue) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue }; return " + "Math.floor(Math.random()*(9999-1000))+1000;")
            bakgmail = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(
                四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2 }; return " + "account+-+bak2+rValue")
            time.sleep(1)
            driver.find_element_by_id("phoneNumberId").clear()
            driver.find_element_by_id("phoneNumberId").send_keys("")
            driver.find_element_by_name("recoveryEmail").click()
            driver.find_element_by_name("recoveryEmail").clear()
            driver.find_element_by_name("recoveryEmail").send_keys(bakgmail)
            driver.find_element_by_id("year").click()
            year = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(
                number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var bakgmail = \"" + str(bakgmail) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2,'bakgmail': bakgmail }; return " + "Math.floor(Math.random()*(2000-1990+1))+1990;")
            driver.find_element_by_id("year").clear()
            driver.find_element_by_id("year").send_keys(year)
            driver.find_element_by_id("month").click()
            moth = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(
                無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var bakgmail = \"" + str(bakgmail) + "\";var year = \"" + str(year) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2,'bakgmail': bakgmail,'year': year }; return " + "Math.floor(Math.random()*(12-1+1))+1;")
            Select(driver.find_element_by_id("month")
                   ).select_by_visible_text(moth + u" 月")
            driver.find_element_by_id("day").click()
            day = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(
                無法使用電話) + "\";var code = \"" + str(code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var bakgmail = \"" + str(bakgmail) + "\";var year = \"" + str(year) + "\";var moth = \"" + str(moth) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2,'bakgmail': bakgmail,'year': year,'moth': moth }; return " + "Math.floor(Math.random()*(28-1+1))+1;")
            driver.find_element_by_id("day").clear()
            driver.find_element_by_id("day").send_keys(day)
            birthday = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(
                code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var bakgmail = \"" + str(bakgmail) + "\";var year = \"" + str(year) + "\";var moth = \"" + str(moth) + "\";var day = \"" + str(day) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2,'bakgmail': bakgmail,'year': year,'moth': moth,'day': day }; return " + "'" + str(year) + u"'+'年 '+'" + str(moth) + u"'+'月 '+'" + str(day) + u"'+'日'")
            driver.find_element_by_id("gender").click()
            Select(driver.find_element_by_id("gender")
                   ).select_by_visible_text(u"不願透露")
            driver.find_element_by_xpath(
                "//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div/div/div/button/span").click()
            self.is_element_present(
                By.XPATH, "//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div/div/div/button/span")
            time.sleep(1)
            driver.find_element_by_xpath(
                "//div[@id='view_container']/div/div/div[2]/div/div[2]/div/div/div/div/button/span").click()
            # ERROR: Caught exception [ERROR: Unsupported command [appendToCSV | google.csv | ${user}, ${account}, ${password}, ${number}, ${birthday}, ${bakgmail}]]
            cont = driver.execute_script("var google = \"" + str(google) + "\";var cont = \"" + str(cont) + "\";var sms = \"" + str(sms) + "\";var myArray = \"" + str(myArray) + "\";var rand = \"" + str(rand) + "\";var fistname = \"" + str(fistname) + "\";var myArray2 = \"" + str(myArray2) + "\";var last1 = \"" + str(last1) + "\";var last2 = \"" + str(last2) + "\";var lastname = \"" + str(lastname) + "\";var user = \"" + str(user) + "\";var account = \"" + str(account) + "\";var password = \"" + str(password) + "\";var 是否需要輸入電話 = \"" + str(是否需要輸入電話) + "\";var 帳號 = \"" + str(帳號) + "\";var errphone = \"" + str(errphone) + "\";var 四方餘額 = \"" + str(四方餘額) + "\";var number = \"" + str(number) + "\";var 無法驗證號碼 = \"" + str(無法驗證號碼) + "\";var 無法使用電話 = \"" + str(無法使用電話) + "\";var code = \"" + str(
                code) + "\";var rValue = \"" + str(rValue) + "\";var bak2 = \"" + str(bak2) + "\";var bakgmail = \"" + str(bakgmail) + "\";var year = \"" + str(year) + "\";var moth = \"" + str(moth) + "\";var day = \"" + str(day) + "\";var birthday = \"" + str(birthday) + "\";var storedVars = { 'google': google,'cont': cont,'sms': sms,'myArray': myArray,'rand': rand,'fistname': fistname,'myArray2': myArray2,'last1': last1,'last2': last2,'lastname': lastname,'user': user,'account': account,'password': password,'是否需要輸入電話': 是否需要輸入電話,'帳號': 帳號,'errphone': errphone,'四方餘額': 四方餘額,'number': number,'無法驗證號碼': 無法驗證號碼,'無法使用電話': 無法使用電話,'code': code,'rValue': rValue,'bak2': bak2,'bakgmail': bakgmail,'year': year,'moth': moth,'day': day,'birthday': birthday }; return " + str(cont) + "+1")
            time.sleep(2)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
