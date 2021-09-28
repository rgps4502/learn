# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import codecs
from itemadapter import adapter
from itemadapter.adapter import ItemAdapter
from requests.api import request
from requests.models import Response
from scrapy.exceptions import DropItem
from scrapy.http.request import Request


class AnimePipeline:
    def process_item(self, item, spider):
        # adapter = ItemAdapter(item)
        # if adapter.get('title'):
        #     if adapter.get('title'):
        #         adapter['title'] = adapter['title']
        #     return item
        # else:
        #     raise DropItem('丟棄')
        # open('D:/下載/123.zip', 'wb').write(item.content)

        return item


class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = codecs.open('123.zip', 'wb', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # if spider.name == 'anime':
        # line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        order = '443557'
        file_url = "https://cheapsslsecurity.com/client/orderdtl.html?orderdetailid=" + \
            order+"&isdownload=true"
        myfile = request.get(file_url, Response.cookies)
        self.file.write(myfile.content)
        return item
