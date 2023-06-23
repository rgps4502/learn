# 線程是進程中執行代碼的一個分支 需要CPU進行調度完成
# 線程模塊
import multiprocessing
import threading
import time
import os


def dance():
    for i in range(3):
        print('跳舞')
        time.sleep(1)


def sing(count, times):

    for i in range(count):
        print('在唱歌')
        time.sleep(times)


if __name__ == '__main__':
    # 創建子線程
    sing_threed = threading.Thread(target=sing, args=(3, 1))
    dance_threed = threading.Thread(target=dance)

    # 開啟線程
    dance_threed.start()
    sing_threed.start()
