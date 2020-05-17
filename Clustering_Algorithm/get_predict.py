import joblib
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


def get_text_tfidf_matrix(corpus):
    """
    获取tfidf矩阵
    :param corpus:
    :return:
    """
    tf = CountVectorizer.fit_transform(corpus)
    tfidf = TfidfTransformer.fit_transform(tf)

    # 获取词袋中所有词语
    # words = self.vectorizer.get_feature_names()

    # 获取tfidf矩阵中权重
    weights = tfidf.toarray()
    return weights

def preprocess_data(corpus_path):
    """
    文本预处理，每行一个文本
    :param corpus_path:
    :return:
    """
    corpus = []
    with open(corpus_path, 'r', encoding='utf-8') as f:
        corpus += [line.strip() for line in f.readlines()]
    return corpus

def keams_predict(filepath: str):
    clf = joblib.load('km.pkl')
    corpus = preprocess_data(filepath)
    weights = get_text_tfidf_matrix(corpus)

    rlt_list = clf.fit_predict(weights)
    print(rlt_list)


if __name__ == '__main__':
    keams_predict(r'C:\Users\叫乌鸦的少年怪\Desktop\content.txt')

