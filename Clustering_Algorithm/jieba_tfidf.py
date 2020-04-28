import jieba
import jieba.analyse

with open('学习-csdn.txt', 'r', encoding='utf-8') as txt:
    data = txt.read()
keywords = jieba.analyse.extract_tags(data, topK=400, withWeight=True, allowPOS=('n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd'))

# print(type(keywords))
# <class 'list'>

for item in keywords:
    print(item[0], item[1])
