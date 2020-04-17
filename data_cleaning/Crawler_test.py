from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content


cx = Extractor(threshold=90)
html = cx.getHtml(
    "https://blog.csdn.net/Winterto1990/article/details/51220307")
content = cx.filter_tags(html)
# print(content)
s = cx.getText(content)

data = clean_content(s)
print(data)

# TODO: 给爬虫新增代理；
#       增加文本输出；
#       文本语料库！！
