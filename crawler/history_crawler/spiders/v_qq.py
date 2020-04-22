# -*- coding: utf-8 -*-
import scrapy, os, requests
from crawler.history_crawler.items import V_qqItem
from Settings import HEADERS
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content
import time

# 爬取380条视频信息

class VQqSpider(scrapy.Spider):
    name = 'v_qq'
    allowed_domains = ['v.qq.com']
    start_urls = ['http://v.qq.com/']

    def parse(self, response):
        item = V_qqItem()
        urls = []
        url_list = response.xpath('//*[@id="mod_main_nav"]/div/div/a/@href').extract()
        for url in url_list:
            if url[0] == '/' and not url[0:4] == "http":
                urls.append(f"http://v.qq.com{url}")
        url_list2 = response.xpath('//*[@class="mod_row_box"]/div[2]/div/div/a/@href').extract()
        urls = urls + url_list2
        item['urls'] = urls
        for i in range(len(item['urls'])):
            try:
                res = requests.get(item['urls'][i], headers=HEADERS)
                if res.ok:
                    res.encoding = 'utf-8'
                    html = res.text
                    ex = Extractor(threshold=3)
                    content = ex.filter_tags(html)
                    data = clean_content(ex.getText(content))
                    with open(f"E:/c++/毕业设计开发日志/06.文本数据集/娱乐/视频/{i}.txt", 'w', encoding="utf-8") as txtfile:
                        txtfile.write(data)
                    print(f"第{i}个网页爬取完毕")
                    time.sleep(2)
            except Exception as e:
                print(f"第{i}个文章错误，链接{item['urls'][i]}，错误原因{e}")
        print(f"共{i}个视频页面信息爬取完毕")


if __name__ == '__main__':
    os.system("scrapy runspider v_qq.py")