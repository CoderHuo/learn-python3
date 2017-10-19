# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs


class SpyPipeline(object):
    def __init__(self):
        self.file = codecs.open('example.json', 'w', encoding='utf-8')
        self.count = 1

    def process_item(self, item, spider):
        print(self.count)
        self.count +=1
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_close(self, spider):
        self.file.close()
