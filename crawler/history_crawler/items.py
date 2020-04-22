# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HistoryCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CsdnItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    # content = scrapy.Field()

class V_qqItem(scrapy.Item):
    urls = scrapy.Field()