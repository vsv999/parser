# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class AllocineTestPipeline(object):
    def open_spider(self, spider):
        self.films = open('films.json', 'a')
        self.series = open('series.json', 'a')

    def close_spider(self, spider):
        self.films.close()
        self.series.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        if item['type'] == 'Movie':
            self.films.write(line)
        else:
            self.series.write(line)
        return item
