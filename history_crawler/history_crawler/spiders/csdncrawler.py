# -*- coding: utf-8 -*-
import scrapy


class CsdncrawlerSpider(scrapy.Spider):
    name = 'csdncrawler'
    allowed_domains = ['www.csdn.net']
    start_urls = ['http://www.csdn.net/']
    # TODO 增加csdn爬虫
    def parse(self, response):
        pass
