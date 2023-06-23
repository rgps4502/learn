import win32api
import win32con
import win32gui
import time

# 窗口位置变化回调函数
def window_position_callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
    if event == win32con.EVENT_OBJECT_LOCATIONCHANGE:
        # 获取窗口位置
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top

        # 自动调整点击坐标
        adjust_click_coordinates(hwnd, width, height)

# 自动调整点击坐标
def adjust_click_coordinates(hwnd, window_width, window_height):
    # 窗口中心坐标
    center_x = window_width // 2
    center_y = window_height // 2

    # 点击方位偏移量
    offset = 50

    # 点击窗口的各个方位
    click_positions = [
        (center_x, center_y - offset),         # 北
        (center_x + offset, center_y - offset), # 东北
        (center_x + offset, center_y),          # 东
        (center_x + offset, center_y + offset), # 东南
        (center_x, center_y + offset),          # 南
        (center_x - offset, center_y + offset), # 西南
        (center_x - offset, center_y),          # 西
        (center_x - offset, center_y - offset)  # 西北
    ]

    # 在此处添加其他方位的点击坐标

    # 执行点击操作
    for x, y in click_positions:
        click_at_position(hwnd, x, y)

# 执行点击操作
def click_at_position(hwnd, x, y):
    left, top, _, _ = win32gui.GetWindowRect(hwnd)
    win32api.SetCursorPos((left + x, top + y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# 监听窗口位置变化
def listen_window_position_changes(hwnd):
    event_min = win32con.EVENT_MIN
    event_max = win32con.EVENT_MAX
    event_flags = win32con.WINEVENT_OUTOFCONTEXT

    # 注册窗口位置变化的回调函数
    win32gui.SetWinEventHook(
        win32con.EVENT_OBJECT_LOCATIONCHANGE,
        win32con.EVENT_OBJECT_LOCATIONCHANGE,
        0,
        window_position_callback,
        hwnd,
        0,
        event_flags
    )

# 示例用法
hwnd = '592530'  # 获取游戏窗口的句柄

# 监听窗口位置变化并自动调整点击坐标
listen_window_position_changes(hwnd)

# 此处可以添加其他逻辑，例如循环运行游戏或其他操作

# 等待窗口位置变化
while True:
    time.sleep(1)
