import os
from time import sleep
import win32api
import win32gui
import win32process
import cv2
import mss
import numpy as np
import pyautogui
import win32con
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


# 獲取窗口名稱和句柄
def get_windows_handle():
    # 使用字典來存儲窗口名稱和句柄的對應關係
    window_dict = {}
    # 列舉所有窗口，並調用回調函式處理每個窗口
    win32gui.EnumWindows(enum_windows_callback, window_dict)

    # 找到指定名稱的視窗句柄
    window_handle = None
    for title, handle in window_dict.items():
        if title.strip() == window_title:
            window_handle = handle
            return window_handle
    else:
        return False



def capture_game_screen(hwle):
    with mss.mss() as sct:
        # 獲取遊戲視窗的位置和大小

        game_rect = win32gui.GetWindowRect(hwle)
        x, y, width, height = game_rect

        # 設定 mss 的螢幕區域為遊戲視窗
        monitor = {"top": y, "left": x, "width": width, "height": height}

        # 擷取遊戲畫面
        image = np.array(sct.grab(monitor))

        # 將圖像轉換為 OpenCV 格式
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        return image

    # 比對target_image 是否存在於 game_screen
def compare_images(game_screen, target_image):
    # 將圖像轉換為灰度圖像
    gray_image1 = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配算法進行圖像比對
    result = cv2.matchTemplate(gray_image1, gray_image2, cv2.TM_CCOEFF_NORMED)
    _, similarity, _, _ = cv2.minMaxLoc(result)

    # 根據相似度閾值判斷是否存在目標圖像
    threshold = 0.9  # 相似度閾值，可以根據需要進行調整
    if similarity >= threshold:
        return True
    else:
        return False


# 點擊圖片
def compare_images1(hwnd,game_screen, target_image, threshold=0.9):
    # 將遊戲畫面轉換為灰度圖像
    gray_image1 = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)
    
    # 使用模板匹配算法進行圖像比對

    # 將目標圖像轉換為灰度圖像
    gray_image2 = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_image1, gray_image2, cv2.TM_CCOEFF_NORMED)
    _, similarity, _, max_loc = cv2.minMaxLoc(result)

    # 根據相似度閾值判斷是否存在目標圖像
    if similarity >= threshold:
        # 獲取目標圖像的座標位置
        x, y = max_loc[0], max_loc[1]
        # # 在目標位置進行後臺點擊
        click_at_position(hwnd,x,y)
    
        return True
    else:
        return False

def click_at_position(hwnd,cx, cy):
        long_position = win32api.MAKELONG(cx, cy)#模拟鼠标指针 传送到指定坐标
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起   
        
        
 
# 指定視窗名稱、按鍵和截圖檔案名稱
window_title = "ODIN"
save_filename = "test2.png"

# # 對指定視窗後台發送按鍵消息並進行截圖
# send_key_and_take_screenshot(window_title, key, save_filename)
if __name__ == "__main__":
    # 獲取腳本運行的位置
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 構建截圖的完整路徑
    save_path = os.path.join(script_dir, save_filename)
    windows_handle = get_windows_handle()
    # 檢查是否找到遊戲視窗
    assert windows_handle,f'沒有找到 {window_title} 遊戲視窗'


    game_screen = capture_game_screen(windows_handle)
    # cv2.imwrite("game_screen.png", game_screen)
    # # 讀取要比對的圖像
    target_image = cv2.imread(save_path)
    target_image2 = cv2.imread(script_dir+'\move.png')
    # game_screen = cv2.imread(script_dir+'\screenshot.png')
    print(compare_images(game_screen, target_image2))
    
    similarity_threshold = 0.7
    compare_images1(windows_handle,game_screen, target_image, similarity_threshold)
    # sleep(1)
    # compare_images1(windows_handle,game_screen, target_image2, similarity_threshold)
        # pyautogui.click(target_position)
        # sleep(1.5)
    target_position = pyautogui.locateCenterOnScreen(target_image2)
    sleep(0.5)
    pyautogui.click(target_position)