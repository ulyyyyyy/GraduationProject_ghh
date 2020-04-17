import requests
from Settings import HEADERS
import json
from ProxyPool.proxy_crawl import crawl_freeproxy
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

# Csdn_api,已经爬取了198篇文章

def get_urls():
    url_list = []
    category_list = ['Python', 'JAVA', 'web', 'arch', 'db', 'iot', 'fund']  # 七个模块
    for category in category_list:
        for page in range(3):
            csdn_api = f"https://blog.csdn.net/api/articles?type=more&category=python&shown_offset={page}"
            response = requests.get(csdn_api, headers=HEADERS)
            html = response.text
            data_json = json.loads(html)
            for article in data_json['articles']:
                url_list.append(article['url'])
    return url_list

def parse_urls(url_list: list):
    try:
        for i in range(len(url_list)):
            extractor = Extractor(threshold=90)
            html = extractor.getHtml(url_list[i])
            content = extractor.filter_tags(html)
            data = clean_content(extractor.getText(content))
            with open(f'E:/c++/毕业设计开发日志/06.文本数据集/学习/csdn/{i}.txt', 'w', encoding='utf-8') as txtfile:
                txtfile.write(data)
            print(f"第{i}篇文章处理完毕")
        print(f"共{i}篇文章处理完毕")
    except Exception as error:
        print(error)


if __name__ == '__main__':
    url_list = get_urls()
    parse_urls(url_list)