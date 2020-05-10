import requests
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content
from requests.exceptions import ConnectionError

def parse_url():
    urls = []
    data = []
    length_all = 0
    length_ok = 0
    with open(r"C:\Users\叫乌鸦的少年怪\Desktop\历史记录文件.txt", 'r', encoding='utf-8-sig') as files:
        urls += ["https://" + url[:-1] for url in files.readlines()]

    length_all = len(urls)

    for url in urls:
        try:
            ex = Extractor(threshold=30)
            html = ex.getHtml(url)
            content = ex.getText(ex.filter_tags(html))
            content = clean_content(content)
            data_str = ""
            for _ in content.splitlines():
                data_str += _
            data.append(data_str)
            length_ok += 1
        except ConnectionError:
            print("响应失败")
            # TODO 记录下host
        except Exception as e:
            print(e)
            continue
    with open(r"C:\Users\叫乌鸦的少年怪\Desktop\content.txt", 'w+', encoding='utf-8') as rlt_txt:
        for single_data in data:
            rlt_txt.write(single_data + '\n')

    print(f"成功访问的{length_ok}")
    print(f"一共{length_all}")
    print(f'百分比{length_ok/length_all}')


if __name__ == '__main__':
    parse_url()