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


def sing():

    for i in range(3):
        print('在唱歌')
        time.sleep(1)


if __name__ == '__main__':
    # 當前主進程編號
    print('主進程', os.getpid())

    # 創建子進程
    dance_process = multiprocessing.Process(target=dance)
    sing_process = multiprocessing.Process(target=sing)

    # 執行子進程
    dance_process.start()
    sing_process.start()
