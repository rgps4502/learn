import os
import time
import win32gui
import win32process
import win32api
import win32con
import pyautogui

def enum_windows_callback(hwnd, lParam):
    # 檢查窗口是否可見和有效
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        # 獲取窗口的應用程式ID
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        # 檢查是否為後台運行的應用程式
        if pid != win32api.GetCurrentProcessId():
            # 獲取窗口的標題文字
            window_title = win32gui.GetWindowText(hwnd)
            # 存儲窗口名稱和句柄的對應關係到字典中
            lParam[window_title] = hwnd

def send_key_to_window(hwnd, key):
    # 傳送按鍵消息到指定窗口
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord(key), 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord(key), 0)

def take_screenshot(hwnd, save_path):
    # 對指定窗口進行截圖
    rect = win32gui.GetWindowRect(hwnd)
    x, y, width, height = rect
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(save_path)

def send_key_and_take_screenshot(window_title, key, save_filename):
    # 使用字典來存儲窗口名稱和句柄的對應關係
    window_dict = {}
    # 列舉所有窗口，並調用回調函式處理每個窗口
    win32gui.EnumWindows(enum_windows_callback, window_dict)
    
    # 找到指定名稱的視窗句柄
    window_handle = None
    for title, handle in window_dict.items():
        if title.strip() == window_title:
            window_handle = handle
            break

    if window_handle:
        # 獲取腳本運行的位置
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # 構建截圖的完整路徑
        save_path = os.path.join(script_dir, save_filename)

        while True:
            # 傳送按鍵消息到指定窗口
            send_key_to_window(window_handle, key)
            # 對指定窗口進行截圖
            take_screenshot(window_handle, save_path)
            # 休眠 2 秒
            time.sleep(2)

# 指定視窗名稱、按鍵和截圖檔案名稱
window_title = 'ODIN'
key = 'T'
save_filename = 'screenshot.png'

# 對指定視窗後台發送按鍵消息並進行截圖
send_key_and_take_screenshot(window_title, key, save_filename)
