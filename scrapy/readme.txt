要安裝scrapy先確認以下安裝

easy_install -U pip
pip3 install cryptography
pip3 install scrapy

創建項目
scrapy startproject 專案名稱
ex : scrapy startproject anime

创建一个新的spider
scrapy genspider 名稱 要爬的URL
ex : scrapy genspider mydomain mydomain.com

系統會創建
scrapy.cfg: 项目的配置文件
anime/: 该项目的python模块。之后您将在此加入代码。
anime/items.py: 项目中的item文件.
anime/pipelines.py: 项目中的pipelines文件.
anime/settings.py: 项目的设置文件.
anime/spiders/: 放置spider代码的目录.

第一步定義items 清單欄位的名稱
ex :
    class AnimeItem(scrapy.Item):   class可自行取名稱
    title = scrapy.Field()       #title就是欄位的名稱
    time = scrapy.Field()        #time就是欄位的名稱

第二步創建spider  用yield返回給Item做處理
from typing import Text
import bs4
import scrapy
from bs4 import BeautifulSoup
from anime.items import AnimeItem

class AnumeUpdate(scrapy.Spider):
    name = 'anime'
    start_urls = ['https://myself-bbs.com/portal.php']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        for alls in soup.select('#portal_block_951_content p'):
            animeItem = AnimeItem()
            animeItem['title'] = alls.text
            # print(alls.text)
            yield animeItem

第三步嘗試運行
scrapy crawl anime  一般運行程是
scrapy crawl anime -o anime.json -t json  運作輸出成json格式



shoot
使用過程中會遇到cloudflare跳轉問題
如何在Scrapy中绕过cloudflare bot/ddos
需要安裝並配入腳本中
pip3 install cfscrape