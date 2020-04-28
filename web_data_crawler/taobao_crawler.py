from requests import request
from Settings import HEADERS
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content


if __name__ == '__main__':
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.9.6e3133a31wZTzO&id=585319218965&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=19"
    response = request("GET", url, headers=HEADERS)
    html = response.text
    ex = Extractor(threshold=30)
    content = ex.filter_tags(html)
    data = clean_content(ex.getText(content))
    with open("E:/c++/毕业设计开发日志/06.文本数据集/网购/淘宝/", 'w+', encoding='utf-8') as file:
        file.write(data)
    8