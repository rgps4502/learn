# -*- coding: utf-8 -*
from itertools import count
import subprocess
import sys
import os


# 或取名為google的模擬器編號
def get_windows():
    windows_list = subprocess.getstatusoutput('ldconsole.exe list2')[
        1].split('\n')

    # print(windows_list)

    for a in windows_list:
        if 'google' not in a:
            print('找不到名稱為google的模擬器')
        else:

            for a in windows_list:
                # print(a.split(','))
                if a.split(',')[1] == 'google':
                    return a.split(',')[0]

 # 輸入文字


def inpunt(put):
    subprocess.getstatusoutput(
        'dnconsole.exe action --name google --key call.input --value {0}'.format(put))


if __name__ == '__main__':
    #
    windos_num = get_windows()
    print(windos_num)

    # 輸入文字
    # inpunt('你好')
    # subprocess.getstatusoutput(
    # 'dnconsole.exe pm list packages')
