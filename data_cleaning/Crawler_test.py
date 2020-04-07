from data_cleaning.Extractor import Extractor

cx = Extractor(threshold=55)
html = cx.getHtml(
    "https://www.douyu.com/88660")
content = cx.filter_tags(html)
# print(content)
s = cx.getText(content)
print(s)
# TODO: 给爬虫新增代理；
#       增加文本输出；
#       文本语料库！！
