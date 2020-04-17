import jieba
from data_cleaning.Extractor import Extractor


def stopwordslist():
    """
    调用停用词表
    :return:
    """
    stopwords = [line.strip() for line in open(r'E:\c++\毕业设计开发日志\06.文本数据集\chinesestopwords.txt').readlines()]
    return stopwords


def seg_depart(sentence: str):
    """
    分词
    :param sentence:
    :return:
    """
    # 对文档中每一行进行分词
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


def clean_content(content):
    return seg_depart(content)
