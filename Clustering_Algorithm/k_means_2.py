# -*- coding: utf-8 -*-

import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import joblib
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


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
            corpus += [line.strip() for line in f.readlines()]
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
        # print(corpus)
        weights = self.get_text_tfidf_matrix(corpus)
        #
        clf = KMeans(n_clusters=n_clusters)
        y = clf.fit(weights)
        # 中心点
        print('cluster_center:', clf.cluster_centers_)
        #
        # 每个样本所属的簇
        print(clf.labels_)
        print('list_number label  ')
        # i = 1
        # while i <= len(clf.labels_):
        #     # print(i, '          ', clf.labels_[i - 1])
        #     with open('聚类结果.txt', 'a+', encoding='utf-8') as rlt_txt:
        #         rlt_txt.write(f"{i}          {clf.labels_[i - 1]}\n")
        #     i = i + 1
        #
        # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
        print('inertia:', clf.inertia_)
        #
        # 保存模型
        joblib.dump(clf, 'km.pkl')
        print('模型已保存完毕')

        # 画图
        pca = PCA(n_components=2)
        newData = pca.fit_transform(weights)

        x = []
        y = []
        for i in range(len(corpus)):
            x.append(newData[i][0])
            y.append(newData[i][1])
        plt.plot(x, y, 'or')
        plt.show()


        # 每个样本所属的簇
        # result = {}
        # for text_idx, label_idx in enumerate(y):
        #     if label_idx not in result:
        #         result[label_idx] = [text_idx]
        #     else:
        #         result[label_idx].append(text_idx)
        # return result

    def keams_predict(self, filepath: str):
        clf = joblib.load('km.pkl')

        corpus = self.preprocess_data(filepath)
        # return corpus
        weights = self.get_text_tfidf_matrix(corpus)

        rlt_list = clf.fit_predict(weights)
        print(rlt_list)
        # rlt =
        # if y == 0:


        # return y


if __name__ == '__main__':
    Kmeans = KmeansClustering()
    # Kmeans.kmeans('E:/c++/毕业设计开发日志/06.文本数据集/合集/test/合集3.txt', n_clusters=5)
    Kmeans.keams_predict(r'E:/c++/毕业设计开发日志/06.文本数据集/合集/test/搜索引擎-百度.txt')
    # print(y)
