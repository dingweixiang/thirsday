# -*- coding: utf-8 -*-
import scrapy
from thirsday.items import BoleItem
from scrapy_redis.spiders import RedisSpider

class BoleSpider(RedisSpider):
    name = 'bole'
    allowed_domains = ['jobbole.com']
    # start_urls = ['http://python.jobbole.com/all-posts/']
    redis_key = 'shuaige:rediskey'

    def parse(self, response):
        a_href_list = response.xpath('//a[@class="archive-title"]/@href').extract()
        for a_href in a_href_list:
            url = response.urljoin(a_href)
            yield scrapy.Request(url, callback=self.parse_detail)

        a_next = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        yield scrapy.Request(a_next)

    def parse_detail(self, response):
        item = BoleItem()
        title = response.xpath('//h1/text()').extract_first()
        item['title'] = title
        yield item
        #print(title)
