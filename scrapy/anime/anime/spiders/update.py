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
        # title = soup.find("div", id='portal_block_951_content')  # 尋找哪一個div
        # titles = title.find(["style='width: 180px;'", 'ul'])   # 尋找div裡面的元素
        # for new in titles:
        #         # 在div裡面的ul元素底下找p標籤裡的a標籤裡的title第0位置(他是List也就是第0個)
        #     print(new.p('a')[0]['title'])
        for alls in soup.select('#portal_block_951_content p'):
            animeItem = AnimeItem()
            animeItem['title'] = alls.text
            yield animeItem
