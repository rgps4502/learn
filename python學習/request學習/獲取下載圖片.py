import requests
import os

from requests.sessions import session
# 下載google的圖片


def download_image(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        root = 'G:\vscode學習\python 學習\request學習\image'
        path = root + url.split('/')[-1]
        session = requests.session()
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = session.get(url)

            with open(path, 'wb') as f:  # 打開一個名為wb文件 要存儲jpg的文件 然後定義為f
                f.write(r.content)  # 把返回的二近制內容寫到f這個文件中 (content是二近制)
                f.close()
                print('下載完成')
        else:
            print('已存在')
    except:
        return '連線異常'


url = 'https://t3.ftcdn.net/jpg/02/95/94/94/240_F_295949484_8BrlWkTrPXTYzgMn3UebDl1O13PcVNMU.jpg'
download_image(url)
