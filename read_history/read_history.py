# problem1:直接访问appdata下的history文件需要权限设置。
import sqlite3
import os


def parse_url(url):
    """
    解析url,得到主要url，域名
    :param url:
    :return:
    eg:
    :param:
        https://blog.csdn.net/zyc121561/article/details/77748786
    :return:
        blog.csdn.net
    """
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1]
        if sublevel_split[0:3] != 'www':
            domain = 'www.' + sublevel_split
        else:
            domain = sublevel_split
        return domain
    except IndexError as e:
        print('URL format error!')
        print(e)


def read_history():
    # data_path = r'C:\Users\叫乌鸦的少年怪\AppData\Local\Google\Chrome\User Data\Default'
    data_path = r'C:\Users\叫乌鸦的少年怪\Desktop'
    history_db = os.path.join(data_path, 'history')
    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(select_statement)
    results = cursor.fetchall()
    real_results = []
    for result in results:
        t = parse_url(result[0])
        real_results.append(t)
    f_txt = open(r'C:\Users\叫乌鸦的少年怪\Desktop\his.txt', 'a+')
    for i in real_results:
        f_txt.write(i + '\n')
    f_txt.close()
    print(len(real_results))
    print('Read Chrome History Has Done')


if __name__ == '__main__':
    read_history()