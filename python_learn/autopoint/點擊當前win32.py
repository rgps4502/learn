import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

# 將遊戲視窗設置為前景窗口
game_window = pyautogui.getWindowsWithTitle("Albion Online Client")[0]
game_window.activate()

# 等待一秒鐘以確保視窗被激活
pyautogui.sleep(1)

# 獲取遊戲視窗位置和大小
game_window_left, game_window_top, game_window_width, game_window_height = game_window.left, game_window.top, game_window.width, game_window.height

# 調整截圖的大小和位置以捕捉整個遊戲視窗
game_screen = np.array(ImageGrab.grab(bbox=(game_window_left, game_window_top,
                       game_window_left + game_window_width, game_window_top + game_window_height)).convert("L"))

# 將截圖保存為灰度圖像
cv2.imwrite("albion_online_client.png", game_screen)

# 讀取目標圖像
target_img = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)

# 比對圖像並找到目標圖像
res = cv2.matchTemplate(game_screen, target_img, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

# 如果找到目標圖像，則點擊圖像中心位置
if len(loc[0]) > 0:
    x, y = loc[1][0] + game_window_left, loc[0][0] + game_window_top
    w, h = target_img.shape[::-1]
    x += w // 2
    y += h // 2
    pyautogui.click(x, y)
    print("已點擊a.png的中心位置：", x, y)
else:
    print("沒找到a.png")
