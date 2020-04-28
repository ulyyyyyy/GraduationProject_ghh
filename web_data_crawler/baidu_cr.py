from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content
from time import sleep

with open("C:/Users/叫乌鸦的少年怪/Desktop/words.txt", 'r', encoding='utf-8') as txt:
    words = txt.read()
word_list = words.split('\n')

for i in range(len(word_list)):
    url = f"https://www.baidu.com/s?rsv_idx=1&wd={word_list[i]}&fenlei=256&ie=utf-8"
    ex = Extractor(threshold=40)
    html = ex.getHtml(url)
    content = ex.filter_tags(html)
    data = clean_content(ex.getText(content))
    with open(f"E:/c++/毕业设计开发日志/06.文本数据集/搜索引擎/百度/{i}.txt", 'w', encoding='utf-8') as txtfile:
        txtfile.write(data)
    print(f'第{i}个百度网页爬取完毕')
    sleep(8)
print(f'共{i}个百度网页爬取完毕')

