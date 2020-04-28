import jieba, requests
from Settings import HEADERS
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

if __name__ == '__main__':
    url = 'https://www.huomao.com/1882'
    ex = Extractor(threshold=50)
    html = ex.getHtml(url)
    content = ex.filter_tags(html)
    data = clean_content(ex.getText(content))
    print(data)