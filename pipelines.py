# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from thirsday.mysqlhelper import MysqlHelper

class ThirsdayPipeline(object):
    def process_item(self, item, spider):
        return item

class BolePipeline(object):
    def process_item(self, item, spider):
        (sql, data) = item.get_insert_sql()
        myhelper = MysqlHelper()
        myhelper.execute_modify_sql(sql, data)
        return item
