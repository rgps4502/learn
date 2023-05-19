#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入PyAutoGUI包
import pyautogui
import time

# 开启PyAutoGUI包的故障安全功能，确保程序可以安全退出
pyautogui.FAILSAFE = True
# 设置PyAutoGUI包每一步的操作延时为1.5秒，防止键鼠操作太快
pyautogui.PAUSE = 1.5

# 获取当前鼠标的位置
x, y = pyautogui.position()

# 获取当前显示器的分辨率
# pyautogui.size()
# 判断某一个坐标点是否在显示器的显示范围内，若在，返回True，若不在，返回False
# pyautogui.onScreen(60, 60)

# 鼠标点击操作函数，将鼠标绝对移动到坐标点(100, 200)之后点击3次左键，每次点击间隔0.25秒
# 若需要点击右键则button='right'，若需要点击中键则button='middle'
# while True:
x, y = pyautogui.position()
pyautogui.click(x=x, y=y, button='left',
                clicks=99999999999999999999999999999999999999999999999999, interval=6)


# hwnd = win32gui.FindWindow(None, 'Albion Online Client')
'G:\GitHub\learn\python學習\自動點擊\w.png'
