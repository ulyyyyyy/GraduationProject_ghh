from Settings import HEADERS
import requests
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content
import time

if __name__ == '__main__':
    with open('C:/Users/叫乌鸦的少年怪/Desktop/his.txt', 'r', encoding='utf-8') as txt:
        url_list = txt.readlines()

    for i in range(len(url_list)):
        url = "https://" + url_list[i][:-1]
        try:
            response = requests.get(url, headers=HEADERS)
            html = response.text
            ex = Extractor(threshold=30)
            content = ex.filter_tags(html)
            data = clean_content(ex.getText(content))
            with open(f"E:/c++/毕业设计开发日志/06.文本数据集/网购/淘宝/{i}.txt", 'w+', encoding='utf-8') as file:
                file.write(data)
            print(f"第{i+1}个淘宝网页爬取成功")
            time.sleep(3)
            response.close()
        except Exception as e:
            print(e)
