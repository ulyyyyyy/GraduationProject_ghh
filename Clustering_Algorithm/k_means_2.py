# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.externals import joblib
from sklearn.cluster import KMeans


class KmeansClustering():
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.transformer = TfidfTransformer()

    def preprocess_data(self, corpus_path):
        """
        文本预处理，每行一个文本
        :param corpus_path:
        :return:
        """
        corpus = []
        with open(corpus_path, 'r', encoding='utf-8') as f:
            for line in f:
                corpus.append(' '.join([word for word in jieba.lcut(line.strip())]))
        return corpus

    def get_text_tfidf_matrix(self, corpus):
        """
        获取tfidf矩阵
        :param corpus:
        :return:
        """
        tfidf = self.transformer.fit_transform(self.vectorizer.fit_transform(corpus))

        # 获取词袋中所有词语
        # words = self.vectorizer.get_feature_names()

        # 获取tfidf矩阵中权重
        weights = tfidf.toarray()
        return weights

    def kmeans(self, corpus_path, n_clusters=5):
        """
        KMeans文本聚类
        :param corpus_path: 语料路径（每行一篇）,文章id从0开始
        :param n_clusters: ：聚类类别数目
        :return: {cluster_id1:[text_id1, text_id2]}
        """
        corpus = self.preprocess_data(corpus_path)
        weights = self.get_text_tfidf_matrix(corpus)

        clf = KMeans(n_clusters=n_clusters)
        clf.fit(weights)

        print('cluster_center:', clf.cluster_centers_)

        # 每个样本所属的簇
        # print(clf.labels_)
        print('list_number label  ')
        i = 1
        while i <= len(clf.labels_):
            # print(i, '          ', clf.labels_[i - 1])
            with open('聚类结果.txt', 'a+', encoding='utf-8') as rlt_txt:
                rlt_txt.write(f"{i}          {clf.labels_[i - 1]}\n")
            i = i + 1

        # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
        print('inertia:', clf.inertia_)

        # 保存模型
        joblib.dump(clf, 'km.pkl')
        joblib.dump(clf, 'km.txt')
        print('模型以保存完毕')

        clf_load = joblib.load('km.pkl')
        y = clf_load.fit_predict(weights)

        # 中心点
        # centers = clf.cluster_centers_

        # 每个样本所属的簇
        # result = {}
        # for text_idx, label_idx in enumerate(y):
        #     if label_idx not in result:
        #         result[label_idx] = [text_idx]
        #     else:
        #         result[label_idx].append(text_idx)
        # return result


if __name__ == '__main__':
    Kmeans = KmeansClustering()
    Kmeans.kmeans('E:/c++/毕业设计开发日志/06.文本数据集/合集/test/合集2.txt', n_clusters=5)