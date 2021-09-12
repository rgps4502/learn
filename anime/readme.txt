使用方法
anime.py 執行一次可以無限執行搭搭配screen


contabl使用
先用anime_all_list.py執行一次
獲取總表all_list.txt跟oldata.txt

crontab設定
*/5 * * * * python3 /root/learn/animetest.py >> /root/learn/log.txt

有問題查看log

animetest.py會調用read.py打開檔案寫入資料
