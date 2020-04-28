from requests import get
from Settings import HEADERS
import json, time
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

if __name__ == '__main__':
    cageList = ['dota2', 'lol', 'Movies', 'ylxx', 'battlegrounds']
    api2 = "https://www.huomao.com/channels/channelnew.json?page=1&game_url_rule=all&labelid=93"
    url_list = []
    urls = []
    url_list.append(api2)
    for cage in cageList:
        url_list.append(f"https://www.huomao.com/channels/channelnew.json?page=1&game_url_rule={cage}")

    for url in url_list:
        res = get(url, headers=HEADERS)
        res.encoding = 'utf-8'
        data = json.loads(res.text)
        channelList = data['data']['channelList']
        for i in range(len(channelList)):
                room_id = channelList[i]['room_number']
                urls.append(f"https://www.huomao.com/{room_id}")
    for i in range(len(urls)):
        try:
            ex = Extractor(threshold=40)
            html = ex.getHtml(urls[i])
            content = ex.filter_tags(html)
            data = clean_content(ex.getText(content))

            with open(f"E:/c++/毕业设计开发日志/06.文本数据集/娱乐/直播/{i+100}.txt", 'w', encoding="utf-8") as txt:
                txt.write(data)
            print(f"火猫直播第{i}个房间处理完毕")
        except Exception as e:
            print(e)
        time.sleep(5)
    print(f"火猫直播共{i}个房间处理完毕")

