# -*- coding: utf-8 -*-
import scrapy
from crawler.history_crawler.items import CsdnItem

class CsdncrawlerSpider(scrapy.Spider):
    name = 'csdncrawler'
    allowed_domains = ['www.csdn.net']
    start_urls = ['https://www.csdn.net/nav/python']

    # TODO 增加csdn爬虫
    def parse(self, response):
        item = CsdnItem()
        item['title'] = response.xpath('//*[@id="feedlist_id"]/li[1]/div/div/h2/a/text()').extract()
        item['url'] = response.xpath('//*[@id="feedlist_id"]/li[1]/div/div/h2/a/@href').extract()
        print(item['title'] + item['url'])
        pass
