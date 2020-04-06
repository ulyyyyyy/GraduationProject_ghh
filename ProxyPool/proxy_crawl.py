import requests
import urllib3
from bs4 import BeautifulSoup as bs
import re
from Settings import HEADERS

def crawl_xici():
    """
    实现爬取西刺代理的功能。
    西刺代理：http://www.xicidaili.com
    :return:爬取的代理数据
    """
    urls = 'https://www.xicidaili.com/{}'
    items = []
    proxy = []
    for page in range(1, 3):
        items.append(("wt/{}".format(page), 'http://{}'))
        items.append(("wn/{}".format(page), 'https://{}'))
    for item in items:
        proxy_type, host = item
        url = urls.format(proxy_type)
        html = requests.get(url, headers=HEADERS).text
        soup = bs(html, 'lxml')
        data = soup.find_all('tr', attrs={'class': 'odd'})
        for i in range(1, 30):
            ip_res = data[i].td.next_sibling.next_sibling.string    # 这里用了蠢蠢的方法，在相同的标签下用了“下一个”来选择想要的
            port_res = data[i].td.next_sibling.next_sibling.next_sibling.next_sibling.string
            tmp = ip_res + ':' + port_res
            proxy.append(host.format(tmp))
    return proxy


def crawl_zhandaye():
    """
    站大爷代理：http://ip.zdaye.com/dayProxy.html
    :return: 爬取的代理数据
    """
    homepage_url = 'https://www.zdaye.com/dayProxy.html'
    urllib3.disable_warnings()
    html = requests.get(homepage_url, headers=HEADERS, verify=False).content
    html = html.decode('utf-8')
    print(html)
    proxy_url = re.findall('<H3 class="thread_title"><a href="(.*?)">', html, re.S)
    proxy_url = 'https://www.zdaye.com' + proxy_url[0]
    proxy_html = requests.get(proxy_url, headers=HEADERS, verify=False).content
    proxy_html = proxy_html.decode('utf-8')
    proxy = re.findall('<br>(.*?)\@HTTP', proxy_html, re.S)
    return len(proxy)


if __name__ == '__main__':
    data = crawl_xici()
    print(data)
