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

        return item


class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = codecs.open('list.json', 'wb', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # if spider.name == 'anime':
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
