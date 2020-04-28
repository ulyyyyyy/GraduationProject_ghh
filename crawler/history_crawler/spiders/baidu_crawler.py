# -*- coding: utf-8 -*-
import scrapy
from crawler.history_crawler.items import baidu_Item
from time import sleep
import csv
import os


class BaiduspiderSpider(scrapy.Spider):
    name = 'baidu_spider'

    allowed_domains = ['http://www.baidu.com/']

    def __init__(self, keyword=None, search=None, *args, **kwargs):
        super(BaiduspiderSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.search = search
        if self.keyword == None:  # 如果没有指定关键词，那么从文件中读取
            self.ReadKeyword()

    def ReadKeyword(self):  # 设置要包含要搜索关键词的csv文件
        # 关键词csv文件的位置
        filename = "keywords.csv"
        path1 = os.path.dirname(__file__)  # 获取当前文件所在文件夹
        path2 = os.path.dirname(path1) + '\\keyword\\' + filename  # 获取当前文件所在文件夹的父文件夹
        # 打开(创建)文件
        file = open(path2, 'r', newline='', encoding='utf-8-sig')  # 不带newline的话输出总会有一个空行 加入encoding='utf-8-sig'就不会乱码了
        # csv读取
        reader = csv.reader(file)  # 建立csv文件句柄
        self.keywords = []
        for row in reader:
            self.keywords.append(row)
        self.keywords = self.keywords[1:]  # 去掉第一项

    def start_requests(self):
        if self.keyword == None or self.keyword == "":
            for line in self.keywords:
                line = (line[0]).split()
                keyword = "|".join(line)
                start_urls = "http://www.baidu.com/s?rtt=1&word={0}&rn=10&bsst=1&cl=2&tn=news&rsv_dl=ns_pc"

                U = start_urls.format(keyword)
                yield scrapy.Request(url=U, meta={'keyword': " ".join(line)}, callback=self.parse, dont_filter=True)

                sleep(0.1)  # 设置一个时间间隔，太快了不好
        else:
            start_urls = "http://www.baidu.com/s?rtt=1&word={0}&rn=10&bsst=1&cl=2&tn=news&rsv_dl=ns_pc"
            U = start_urls.format(self.keyword)
            yield scrapy.Request(url=U, meta={'keyword': self.keyword.replace("|", " ")}, callback=self.parse,
                                 dont_filter=True)
            sleep(0.1)  # 设置一个时间间隔，太快了不好

    def parse(self, response):
        # 处理百度verify重定向问题  百度会限制单ip的爬取速率，所以遇到重定向到verify就延时一段时间再重新请求
        if response.status in [301, 302] and "verify" in response.url:
            sleep(1)  # 延时一段时间再重新请求
            yield scrapy.Request(url=response.request.url, meta={'keyword': response.meta['keyword']},
                                 callback=self.parse, dont_filter=True)

        for section in response.xpath('//div[@class="result" and @id]'):
            item = BaidunewsSpiderItem()
            item['keyword'] = response.meta['keyword']  # 标注关键词
            try:
                info = section.xpath('.//a')[0]
                item['link'] = info.xpath('@href').extract()[0]
            except:
                item['link'] = ""

            try:
                res_title = section.xpath('.//h3/a')
                item['title'] = (res_title[0].xpath('string(.)').extract_first()).strip('\n\t \'')
            except:
                item['title'] = ""

            try:
                b = section.xpath('.//div[@class="c-summary c-row " ]')
                if len(b) == 0:
                    b = section.xpath('.//div[@class="c-summary c-row c-gap-top-small"]')
                S = b.xpath('string(.)').extract()[0]
                S = S.replace("\n", " ").replace("\t", " ").replace("\xa0", " ")
                List = S.split()
                List.pop()  # 去除百度快照
                item['platform'] = List[0]
                item['date'] = List[1]
                item['time'] = List[2]
                item['brief'] = "".join(List[3:])

            except:
                item['date'] = ""
                item['platform'] = ""
                item['brief'] = ""
                item['time'] = ""
            yield scrapy.Request(url=item['link'], meta={'item': item}, callback=self.parse_next, dont_filter=True)

        # 解析出下一页的url继续请求
        next_pageURL = response.xpath('//p[@id="page"]/a[@class="n"]')
        # 因为 上一页和下一页的标签都是class=n 如果只有一者出现要单独讨论，否则可能死循环
        if len(next_pageURL) == 0 or (
                len(next_pageURL) == 1 and "上一页" in next_pageURL[0].xpath('./text()').extract()[0]):
            pass
        else:
            next_pageURL = next_pageURL[-1].xpath('@href').extract()[0]
            yield scrapy.Request(url="http://www.baidu.com" + next_pageURL, meta={'keyword': response.meta['keyword']},
                                 callback=self.parse, dont_filter=True)

    def parse_next(self, response):  # 爬取正文的深度只有一层，所以如果正文中有翻页就只能爬取第一页的内容
        item = response.meta['item']
        item['link'] = response.url  # 获取真实的url地址 地址为空则直接返回空的item
        if item['link'] == '':
            yield item

        b = []  # 爬取正文的字符串列表
        string = ""  # 目标正文的字符串
        for path_str in path_list:
            a = response.xpath(path_str)
            if len(a) != 0:  # 爬取正文数据 找到了就分析，否则继续寻找
                b = a.xpath('string(.)').extract()
                string = "".join(b)
                if len(string) > 0:  # 爬取到了有用的正文就可以离开循环
                    break
        item['body'] = string.replace('\n', "").replace('\t', "").replace(" ", "").replace("\r", "")  # 去除没用的关键字
        yield item