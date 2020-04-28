import re, os, time
if __name__ == '__main__':
    path = 'E:/c++/毕业设计开发日志/06.文本数据集/搜索引擎/搜狗/'
    rlt_data = ""

    for root, dirs, files in os.walk(path):
        for file in files:
            rlt_data = ''
            with open(path + file, 'r', encoding='utf-8') as txt:
                data = txt.readlines()
            for _ in data[:-1]:
                _ = _.replace('\n', "")
                re_space = re.compile(r'[\s]{1,}')
                _ = re_space.sub(' ', _)
                rlt_data += _
            with open(path + '搜索引擎-搜狗.txt', 'a+', encoding="utf-8") as txtfile:
                txtfile.write(rlt_data + "\n")

        print(f"共{len(files)}个数文件写入完毕")