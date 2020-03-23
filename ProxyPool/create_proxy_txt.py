from ProxyPool.proxy_crawl import *

def get_proxy_txt(proxy_source: list):
    with open('proxy.txt', 'w+', encoding='utf-8') as f:
        for ele in proxy_source:
            f.write(ele + "\n")


if __name__ == '__main__':
    get_proxy_txt(crawl_xici())
