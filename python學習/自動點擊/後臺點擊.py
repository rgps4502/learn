
import win32con
import win32api
import win32gui
import time
import pyautogui
# 獲取遊戲視窗的句柄
hwnd = win32gui.FindWindow(None, 'ODIN')

# 獲取遊戲視窗的位置和大小
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

# 计算窗口中心点坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
x = (left + right) // 2
y = (top + bottom) // 2
while True:

    # 點擊x=768, y=432的位置
    pyautogui.click(768, 432)

    time.sleep(5)
