from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content
from time import sleep

with open("C:/Users/叫乌鸦的少年怪/Desktop/words.txt", 'r', encoding='utf-8') as txt:
    words = txt.read()
word_list = words.split('\n')

for i in range(len(word_list)):
    url = f"https://www.sogou.com/web?query={word_list[i]}&ie=utf8&from=index-nologin"
    ex = Extractor(threshold=60)
    html = ex.getHtml(url)
    content = ex.filter_tags(html)
    data = clean_content(ex.getText(content))
    sleep(3)
    with open(f"E:/c++/毕业设计开发日志/06.文本数据集/搜索引擎/搜狗/{i}.txt", 'w', encoding='utf-8') as txtfile:
        txtfile.write(data)
    print(f'第{i}个sogou网页爬取完毕')
print(f'共{i}个sogou网页爬取完毕')

