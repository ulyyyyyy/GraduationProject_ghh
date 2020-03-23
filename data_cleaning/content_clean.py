import jieba


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
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


filename = r'E:\c++\毕业设计开发日志\06.文本数据集\a.txt'
outfilename = r"E:\c++\毕业设计开发日志\06.文本数据集\out.txt"

inputfile = open(filename, 'r', encoding='utf-8')
outputs = open(outfilename, 'w', encoding='utf-8')

for line in inputfile:
    print('-------------------正在分词和去停用词-----------')
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
outputs.close()
inputfile.close()
print("删除停用词和分词成功！！！")