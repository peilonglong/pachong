# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import self as self
from kaoshi.items import KaoshiItem
class KaoshiPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        self.fp = open('kaoshi.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
            self.fp.close()

import pymysql
from scrapy.utils.project import get_project_settings

class MysqlPipeline(object):
    def open_spider(self, spider):
        settings = get_project_settings()
        self.conn = pymysql.Connect(host=settings['HOST'], port=settings['PORT'], user=settings['USER'],
                                    password=settings['PWD'], db=settings['DB'], charset=settings['CHARSET'])
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into tupian(imgage_url,imgage_name,video_author,video_date) values("%s","%s","%s","%s")'%(item['imgage_url'],item['imgage_name'],item['video_author'],item['video_date'])

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
            self.cursor.close()
            self.conn.close()










