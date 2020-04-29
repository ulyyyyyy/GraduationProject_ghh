import csv, time, os

if __name__ == '__main__':
    path = 'E:/c++/毕业设计开发日志/06.文本数据集/合集/test/'
    data_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(path + file, 'r', encoding='utf-8-sig') as txt_file:
                data_list += txt_file.readlines()

    with open(path + '合集.txt', 'w', encoding='utf-8') as new_file:
        for data in data_list:
            new_file.write(data)
    print("ok")
