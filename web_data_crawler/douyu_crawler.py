from requests import get
from Settings import HEADERS
import json
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

if __name__ == '__main__':
    urls = []
    for i in range(5):
        response = get("https://www.douyu.com/japi/weblist/apinc/rec/list?uid=8b6321ddbef037034b351cab00081501&num=20", headers=HEADERS)
        data_json = json.loads(response.text)
        data_url = (data_json['data'])
        for data in data_url:
            urls.append(f"https://douyu.com/{data['roomId']}")
    print(f"共爬取{len(urls)}条房间")
    try:
        for i in range(len(urls)):
            ex = Extractor(threshold=20)
            html = get(urls[i], headers=HEADERS).text
            content = ex.filter_tags(html)
            data = clean_content(ex.getText(content))
            with open(f'E:/c++/毕业设计开发日志/06.文本数据集/娱乐/直播/{i}.txt', 'w', encoding='utf-8') as txtfile:
                txtfile.write(data)
            print(f"第{i}个直播间处理完毕")
        print(f'共{i}个直播间处理完毕')
    except Exception as e:
        print(e)

