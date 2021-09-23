# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from json import encoder
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
import json
import codecs


class AnimePipeline:

    def process_item(self, item, spider):
        if spider.name == "Anime1":
            item['id'] = int(item['id'])
        elif spider.name == "anime":
            pass
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('list.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        # if spider.name == 'anime':
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)

        return item
