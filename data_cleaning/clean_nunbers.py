# 该方法清洗文本中的数字
import re

with open('E:/c++/毕业设计开发日志/06.文本数据集/合集/test/合集2.txt', 'r+', encoding='utf-8') as txt:
    data = txt.read()
    data2 = re.sub('[\d\.\\!{…]*', "", data)
    data3 = re.sub("{ [^\s]+", "", data2)
    data4 = re.sub("(\\[\S]*)", "", data3)
with open('E:/c++/毕业设计开发日志/06.文本数据集/合集/test/合集3.txt', 'w+', encoding='utf-8') as new_txt:
    new_txt.write(data4)