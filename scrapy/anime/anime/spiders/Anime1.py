# * -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy
from typing import Text
import bs4
from bs4 import BeautifulSoup
from anime.items import Anime1Item


class Anime1Spider(scrapy.Spider):
    name = 'Anime1'
    allowed_domains = ['anime1.me']
    start_urls = ['http://anime1.me/']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        anime1Item = Anime1Item()
        x = 1
        for new in soup.select('#recent-posts-6 a'):
            anime1Item['id'] = x
            anime1Item['url'] = new.get('href')
            anime1Item['title'] = new.getText()
            x = x+1
            yield anime1Item
