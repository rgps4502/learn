import os
from time import sleep
import win32gui
import win32process
import win32api
import win32con
import cv2
import mss, glob
import numpy as np
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


def send_key_to_window(hwnd, key):
    if key == "ESC":
        key = win32con.VK_ESCAPE
    else:
        key = ord(key)
    # 傳送按鍵消息到指定窗口
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, key, 0)


# 遊戲視窗截圖
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

# 或取遊戲窗口位置大小
def get_game_windows_x_y(hwnd):
    # 获取游戏窗口位置和大小
    game_rect = win32gui.GetWindowRect(hwnd)

    # game_rect 包含窗口的左上角和右下角坐标
    x = game_rect[0]
    y = game_rect[1]
    width = game_rect[2] - game_rect[0]
    height = game_rect[3] - game_rect[1]
    return game_rect

def get_images_path(script_dir, image_pattern, list=[]):
    try:
        # 使用通配符匹配獲取目標圖像的檔案路徑列表
        image_paths = glob.glob(image_pattern)
        # 讀取目標圖像並存儲到列表中
        for image_path in image_paths:
            image = cv2.imread(image_path)
            if image is not None:
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                list.append(gray_image)
            else:
                print(f"無法讀取圖像：{image_path}")
        if list == []:
            print(str(script_dir) + "images資料夾中沒有任何PNG圖")
        else:
            return list
    except Exception as e:
        print("images請檢察目錄是否錯誤", e)

    # 比對target_image 是否存在於 game_screen


# 當前遊戲視窗圖像比對
def compare_images(game_screen, target_images, wait_list):
    # 將圖像轉換為灰度圖像
    gray_image1 = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)
    # gray_image2 = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)
    threshold = 0.9  # 相似度閾值，可以根據需要進行調整
    # 使用模板匹配算法進行圖像比對
    for gray_image2 in target_images:
        result = cv2.matchTemplate(gray_image1, gray_image2, cv2.TM_CCOEFF_NORMED)
        _, similarity, _, _ = cv2.minMaxLoc(result)

        # 根據相似度閾值判斷是否存在目標圖像

        if similarity >= threshold:
            return True

    # 檢測如果還在採集中或是施放技能條中
    for gray_wait in wait_list:
        result = cv2.matchTemplate(gray_image1, gray_wait, cv2.TM_CCOEFF_NORMED)
        _, similarity, _, _ = cv2.minMaxLoc(result)

        # 根據相似度閾值判斷是否存在目標圖像

        if similarity >= threshold:
            return sleep(1)


# 後臺點擊
def click_at_position(hwnd, cx, cy):
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(
        hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position
    )  # 模拟鼠标按下
    win32api.SendMessage(
        hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position
    )  # 模拟鼠标弹起


# 點擊圖片
def point_images(hwnd, game_screen, target_images, threshold=0.9):
    # 將遊戲畫面轉換為灰度圖像
    gray_image1 = cv2.cvtColor(game_screen, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配算法進行圖像比對

    # 將目標圖像轉換為灰度圖像
    for target_image in target_images:
        # gray_image2 = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(gray_image1, target_image, cv2.TM_CCOEFF_NORMED)
        _, similarity, _, max_loc = cv2.minMaxLoc(result)
        print(max_loc)
        # 根據相似度閾值判斷是否存在目標圖像
        if similarity >= threshold:
            # 獲取目標圖像的座標位置
            x, y = max_loc[0], max_loc[1]
            # # 在目標位置進行後臺點擊
            # click_at_position(hwnd, x, y)
            target_position = pyautogui.locateCenterOnScreen(target_image)
            sleep(0.8)
            pyautogui.click(target_position)
            print(True)
            return True
        else:
            print(False)
            # return False

# 獲取東西南北方位
def get_direction(hwnd):
    game_rect = get_game_windows_x_y(hwnd)
    x, y, width, height = game_rect

    center_x = x + width // 2
    center_y = y + height // 2

    # 点击东西南北方位
    pyautogui.click(center_x , y * 20)  # 北
    # pyautogui.click(center_x, y + height)  # 南
    # pyautogui.click(x, center_y)  # 西
    # pyautogui.click(x + width, center_y)  # 东

    # # 点击东北、东南、西南、西北方位
    # pyautogui.click(x + width, y)  # 东北
    # pyautogui.click(x + width, y + height)  # 东南
    # pyautogui.click(x, y + height)  # 西南
    # pyautogui.click(x, y)  # 西北

    # # 点击四个角落方位
    # pyautogui.click(x, y)  # 左上角
    # pyautogui.click(x + width, y)  # 右上角
    # pyautogui.click(x, y + height)  # 左下角
    # pyautogui.click(x + width, y + height)  # 右下角

    print(True)
    return True



def move(windows_handle, tar_images, tar_image2):
    send_key_to_window(windows_handle, "M")
    sleep(5)
    point_images(windows_handle, capture_game_screen(windows_handle), tar_images)
    sleep(1)
    target_position = pyautogui.locateCenterOnScreen(tar_image2)
    sleep(0.8)
    pyautogui.click(target_position)
    send_key_to_window(windows_handle, "ESC")


# 指定視窗名稱、按鍵和截圖檔案名稱
window_title = "ODIN"
# 按鍵
key = "T"
save_filename = "screenshot.png"
# 獲取腳本運行的位置
script_dir = os.path.dirname(os.path.abspath(__file__))
# 構建截圖的完整路徑
save_path = os.path.join(script_dir, save_filename)

# 獲取image圖
target_image_pattern = os.path.join(script_dir, "images/target", "*.png")
wait_image_pattern = os.path.join(script_dir, "images/wait", "*.png")
aren_image_pattern = os.path.join(script_dir, "images/aren", "*.png")
# 指定目標圖像的檔案路徑模式 獲取所有要比對的PNG圖
target_images = get_images_path(script_dir, target_image_pattern)
wait_images = get_images_path(script_dir, wait_image_pattern)
aren_images = get_images_path(script_dir, aren_image_pattern)

# # 讀取要比對的圖像
tar_images = [
    cv2.imread(script_dir + "\\test.png"),
    cv2.imread(script_dir + "\\test2.png"),
]
tar_image2 = cv2.imread(script_dir + "\\move.png")

if __name__ == "__main__":
    windows_handle = get_windows_handle()
    print(windows_handle)
    # 檢查是否找到遊戲視窗
    assert windows_handle, f"沒有找到 {window_title} 遊戲視窗"
    # point_images(windows_handle,capture_game_screen(windows_handle), aren_images)
    # move(windows_handle, aren_images, tar_image2)

    # send_key_to_window(windows_handle, 'M')
    # 指定目標圖像的檔案路徑模式 獲取所有要比對的PNG圖

    # move(windows_handle, aren_images, tar_image2)
    # counter = 0  # 計數器變數
    # while True:
    #     sleep(0.3)
    #     a = compare_images(
    #         capture_game_screen(windows_handle), target_images,wait_images
    #     )
    #     print(a)
    #     if a == True:
    #         send_key_to_window(windows_handle, key)
    #         sleep(5)
    #         move(windows_handle, aren_images, tar_image2)
    #     else:
    #         counter += 1  # 每次迴圈執行後計數器加1

    #         if counter % 30 == 0:
    #             # 每出現30次後執行某個動作
    #             move(windows_handle, aren_images, tar_image2)

    get_direction(windows_handle)