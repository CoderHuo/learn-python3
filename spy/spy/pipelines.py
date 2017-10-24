# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, codecs


class SpyPipeline(object):
    def __init__(self):
        self.file = open('example.json', 'w', encoding='utf-8')
        self.jobData = {"job": []}
        self.job_location = {}
        self.job_category = {}

    def process_item(self, item, spider):
        self.jobData["job"].append(dict(item))
        self.collect_job(self.job_location, 'workLocation', item)
        self.collect_job(self.job_category, 'category', item)
        return item

    def close_spider(self, spider):
        self.jobData['location'] = self.job_location
        self.jobData['category'] = self.job_category
        line = json.dumps(dict(self.jobData), ensure_ascii=False)
        self.file.write(line)
        self.file.close()

    def collect_job(self, job_dict, key, item):
        if item[key] in job_dict.keys():
            job_dict[item[key]] += int(item['recruitNumber'])
        else:
            # 初始化
            job_dict[item[key]] = int(item['recruitNumber'])
