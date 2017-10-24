# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs


class SpyPipeline(object):
    def __init__(self):
        self.file = open('example.json', 'w', encoding='utf-8')
        self.jobData = {"job":[]}
        #self.job

    def process_item(self, item, spider):
        self.jobData["job"].append(dict(item))
        return item

    def close_spider(self, spider):
        line = json.dumps(dict(self.jobData), ensure_ascii=False)
        self.file.write(line)
        self.file.close()
