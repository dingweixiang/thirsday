# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThirsdayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BoleItem(scrapy.Item):
    title = scrapy.Field()

    def get_insert_sql(self):
        sql = 'INSERT INTO bole_test_2(title) VALUES(%s)'
        data = (self['title'],)
        return (sql, data)
