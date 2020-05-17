# -*- coding: utf-8 -*-

from pandas.tests.extension.numpy_.test_numpy_nested import np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import joblib
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances_argmin
from collections import Counter
from data_cleaning.single_txt_to_one_line import get_txt_to_single
from data_cleaning.content_clean import clean_content
import time

class KmeansClustering:
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
        clf = KMeans(n_clusters=n_clusters, init="k-means++", )
        y = clf.fit(weights)
        # 中心点
        print(clf.labels_)

        # print('cluster_center:', clf.cluster_centers_)
        #
        # 每个样本所属的簇
        # print(clf.labels_)
        # print('list_number label  ')
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

        colors = ['r', 'g', 'y', 'k', 'm']
        x = []
        y = []
        for i in range(len(corpus)):
            plt.plot(newData[i][0], newData[i][1], f'o{colors[clf.labels_[i]]}')
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
        clf = joblib.load(r'E:\c++\pythonWS\GraduationProject\Clustering_Algorithm\km.pkl')

        x_str_labels = ['直播', '搜索', '网购', '学习', '视频']

        corpus = self.preprocess_data(filepath)
        # return corpus
        weights = self.get_text_tfidf_matrix(corpus)
        rlt_list = clf.fit(weights)
        counter = Counter(rlt_list.labels_)
        x_list = []
        for i in list(counter):
            x_list.append(x_str_labels[i])

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.bar(x_list, list(counter.values()), width=0.4)
        plt.xlabel('访问网页分类', fontsize=8)
        plt.ylabel('访问次数', fontsize=8)
        plt.title('上网行为分析图', fontsize=10)
        for a, b in zip(x_list, list(counter.values())):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
        plt.show()
        # plt.savefig(r'E:\c++\pythonWS\GraduationProject\analyse_result.png')

    def get_labels(self):
        clf = joblib.load('km.pkl')
        with open('聚类结果.txt', 'a+', encoding='utf-8') as file:
            for i in clf.labels_:
                file.write(str(i) + "\n")

    def single_content_analyse(self, corpus):
        content = get_txt_to_single(corpus)
        cut_content = clean_content(content)
        result = self.keams_single_analyse(cut_content)
        print(result)


    def keams_single_analyse(self, corpus):
        clf = joblib.load(r'E:\c++\pythonWS\GraduationProject\Clustering_Algorithm\km.pkl')
        x_str_labels = ['直播', '搜索', '网购', '学习', '视频']
        corpus = [corpus, corpus, corpus, corpus, corpus, corpus]
        weights = self.get_text_tfidf_matrix(corpus)
        rlt_list = clf.fit(weights)
        result = max(rlt_list.labels_)
        return x_str_labels[result]


if __name__ == '__main__':
    Kmeans = KmeansClustering()
    # Kmeans.kmeans('E:/c++/毕业设计开发日志/06.文本数据集/合集/test/合集3.txt', n_clusters=4)
    # Kmeans.keams_predict(r'C:\Users\叫乌鸦的少年怪\Desktop\content.txt')
    # Kmeans.get_labels()
    Kmeans.single_content_analyse("""版权 声明 本文 博主 原创 文章 CC  BY SA 版权 协议 转载 请 附上 原文 出处 链接 声明  本文 链接 https blog csdn net Federal ding article details   include bits std c++ h  using namespace std  int main  ios sync with stdio false  int T  cin T  while T  int a b c d  cin a b c d  cout b c c endl  return  include bits std c++ h  using namespace std  int main  ios sync with stdio false  int T  cin T  while T  long long x a b f  cin x a b  for int i i a && f i ++  if x b  f  else  x  x   cout x endl  if x b  f  if f cout NO endl  else cout YES endl  return  啊啊啊 比赛 wa 次 起床 之后 发现 数组 开小 抓狂 QAQ  include bits std c++ h  using namespace std  vector int a  y   int dis  c  n   void dist int p  cout p endl  int len a p size  for int i i len i ++  int t a p back  a p pop back  if dis t | | t continue  dis t dis p  dist t  return  void lens int p  cout p endl  int len y p size  if p   for int i i len i ++  int t y p back  y p pop back  if c t  | | t continue  c p ++  lens t  c p c t  for int i i len i ++  int t y p back  y p pop back  if t continue  lens t  c p c t  struct rule  bool operator const a const a const  return dis a c a dis a c a  int main  ios sync with stdio false  int T  cin T  while T  int x k t b  long long sum  cin x k  for int i i x i ++  cin t b  a t push back b  a b push back t  y t push back b  y b push back t  for int i i x i ++  dis i  c i  n i i  c  dist  lens  for int i i x i ++  c i  sort n n x rule  for int j j x j ++  cout n j dis n j c n j endl  for int i i k i ++  sum dis n i c n i  cout sum endl  return  文章 举报  Orink  发布 篇 原创 文章 获赞  访问量   准备 长时间 期末考 萎掉 技术 考了 年级  名  IdentifyingWood 一遍 找 过去 # include include include i  Zarxdy  include include include include include include include include using namespace std define  u 专栏  Hello Im Peter # include include include include include include include include include include #  peteryuanpan 专栏  problem link 枚举 长度 L 计算 一段 长度 L 差值 最大公约数 差值 除以 最大公约数 当前 段 关键字 段 比较 关键字 转化 pro  weixin  博客  一次 比赛 结束 写 完  sad 感觉 题目 描述 尴尬 说 机器 每天 生产 a 东西 零件 坏 每天 只能 生产 b 东西 看到 说 机器 坏 Pi 修理 日期  humeay 博客  http codeforces com contest  problem B 原题 简单 傻逼读 错题 题目 n 序列 序列 问 移动 整  缺氧  selenium 定位 时报 错 selenium common exceptions ElementClickInterceptedException Message Element span  __ tian __ 博客  http community topcoder com stat c problem statement pm  rd  这道 题目 容易 贪心 方向 思考 很难  weixin  博客  http community topcoder com stat c problem statement pm  rd  容易 枚举 令 p q 表示 以其为 结  weixin  博客  A Orchestra 题目 连接 http www codeforces com contest  problem ADescriptionPaul is at the orchestra   weixin  博客  感觉 全世界 营销 文都 推 Python 找 不到 工作 机构 站 推荐 工作 笔者 冷静 分析 多方 数据 想 说 超越 老牌 霸主 Java 过去 几年 间 Python 寄予厚望 事实  CSDN 学院  大学 四年 课本 课本 学习 特别 自学 善于 搜索 网上 资源 辅助 必要 下面 几年 私藏 资源 网站 贡献 主要 电子书 搜索 实用工具 在线视频  帅地  今年  误导 咨询 猎头 圈内 好友 年  岁 几位 老 程序员   舍 老脸 揭 伤疤   希望 帮助 记得 帮 点赞 目录 人生 一次 一次 伤害 猎头 界 真  启舰  文章 目录 Pillow 模块 讲解 Image 模块  打开 图片 显示 图片  创建 简单 图像  图像 混合 透明度 混合 遮罩 混合  图像 缩放 像素 缩放 尺寸 缩放   ZackSock 博客  相信 时不时 听到 程序员 猝死 消息 听 不到 产品 经理 猝死 消息 这是 先 百度搜 一下 程序员 猝死 出现  多万条 搜索 搜索 一下 产品 经理 猝死  万条 搜索 搜  曹银飞 专栏  每天 收到 读者 私信 问 二哥 推荐 学习 网站 最近 浮躁 手头 网站 看烦 想 看看 二哥 新鲜 货 今天 一早 做 恶梦 梦到 老板 辞退 说 公司 辞退 老  沉默 王二  遗憾 春节 注定 刻骨铭心 新型 冠状病毒 每个 神经 紧绷 武汉 白衣天使 尤其 值得 尊敬 窝 家里 程序员 外出 外出 社会 做出 最大 贡献 读者  沉默 王二  之前 做过 不到 月 外包  第一天 释放  年 剩 天 外包 公司 离职 谈谈 看法 定义 一下 前途 稳定 工作 环境 不错 收入 能够 项目 中 不断  dotNet 全栈 开发  一辆 装  部 智能手机 手 拉车 一位 柏林 艺术家 一条 空荡荡 街道 骇 一次 谷歌 地图 成功 虚拟 堵车 柏林 艺术家 Simon Weckert 最近 Google 地图 功能 代替 路障 禁  德国 IT 事  说起 B 站 九 眼里 宝藏 存在 放年 假宅 在家 时 一天 刷 小时 不在话下 更 别提 今年 跨 年 晚会 跪 完 最早 聚 B 站 追番 上面 刷 欧美 新歌 漂亮 小姐姐 舞蹈 视  九章 算法 博客  几年 经验 程序员 之前 发展 却是 一头雾水 知道 主流 技术 知道 工作 迎合 主流 技术 迎合 公司 发展 感触 两年 坚持 学习 迎合 公司 发展 前提 学  JAVA 圈 博客  学弟 一家 小型 互联网 公司 做 Java 后端 开发 最近 公司 新来 技术 总监 这位 技术 总监 技术细节 看重 公司 之后 推出 政策 定义 开发 规范 日志 规范 要求 统一  HollisChuang s Blog  字节 跳动 创立  年 月 目前 仅 年 时间 十几个 工程师 研发 上百人  余人 产品线 内涵 段子 今日 头条 今日 特卖 今日 电影 产品线 产品 背景 今日 头条 用户 提供 个性化 资讯 客  作 独立 连续 思考者  一名 程序员 青春年华  岁 回到 三线 城市 洛阳 工作 已经 年 有余 一不小心 暴露 实际 年龄 老 读者 知道 驻颜有术 上次 房子 业务员 肯定 地说 小哥 肯定 今年  沉默 王二  最近 看到 程序员 副业 赚钱 文章 出 点子 网上 找 项目 做 兼职 录制 课程 网上 平台 售卖 免费 推广 赚 广告费 写 付费 专栏 文章 寻找 漏洞 获取 赏金  码农 翻身  今天下午 朋友圈 看到 发 github 羊毛 一时 没 明白 怎么回事 百度 搜索 一下 原来 真有 回事 资源 主义 羊毛  刀刷 爆 朋友圈 知道 朋友圈 有没有 看到 类似 消息  dotNet 全栈 开发  工作 中 误删 数据 数据库 一定 需要 跑 路 未必 程序员 一定 学会 自救 神不知鬼不觉 数据 找回 mysql 数据库 中 知道 binlog 日志 记录 数据库 操作  平头 哥 技术 博文  临近 月份 金三银 四 换 工作 高峰期 往年 月份 今年 特殊 多方 渠道 了解 月份 关注 公众 号 朋友 了解 公众 号 年 时间 发 Elastic S  铭毅 天下 公众 号 同名  loonggg 读完 需要 分钟 速读 仅 需 分钟 今天 刷 爆 朋友圈 微博 IT 新闻 估计 朋友 应该 已经 看到 程序员 删库 跑 路 事情 发生 调侃 真实 事情 微盟 官网 发布 公  非 著名 程序员  跳槽 每个 职业生涯 一部分 HR 说 三年 两跳 已经 跳槽 频繁 阈值 市面上 程序员 不到 一年 跳槽 担心 影响 履历 PayScale 之前 发布 员工 最短 任期 公  九章 算法 博客  老生常谈 梗  争论 一天天 说 在座 人才 图 红色 箭头 new 产生 字符串 宜春 时 会先 常量 池中 查找 是否 已经  宜春  昨天早上 远程 方式 review 两名 新来 同事 代码 大部分 代码 写 很漂亮 严谨 注释 到位 这令 满意 看到 人写 switch 语句 时 忍不住 破口大骂  沉默 王二  小汤山 医院 医院 早 拆 剩 一片 芦苇 荒地 四周 悄然 兴建 温泉 别墅 原本 不该 存在 小汤山 医院  年 最痛 伤痕 这是 最近 突然 火 国产 记录片 非典 十年 祭 记录 一场 完全 意  纯洁 微笑  微信 收到 一位 读者 小涛 留言 意思 高中 学历 经过培训 找到 一份 工作 难 胜任 考虑 辞职 找 一份 能力 胜任 实习 工作 下面 留言 一部分 内容 二哥  年 高中 毕  沉默 王二  互联网 公司 工作 很难 避免 黑客 打交道 呆 两家 互联网 公司 每月 每天 每分钟 黑客 公司 网站 扫描 寻找 Sql 注入 缺口 寻找 线上 服务器 存在 漏洞 大部分  纯洁 微笑  loonggg 读完 需要 分钟 速读 仅 需 分钟 校长 之前 讲过 这年头 肯 动脑 肯 行动 程序员 技术 赚钱 方式 多种 仅仅 公司 出卖 劳动 时  非 著名 程序员  VC Venture Cup  Final Round Div Edition D Factory Repairs 线段 树     阅读数   cf VC Venture Cup  Final Round Div Edition B sland Puzzle 水题 hash     阅读数   selenium 报错     阅读数   vue 递归 渲染 页面     阅读数   TopCoder SRM DIV pt ShoppingSurveyDiv 二分 搜索     阅读数   TopCoder SRM DIV pt SimilarRatingGraph 枚举 边界 处理     阅读数  VC Venture Cup  Final Round Div Edition A Orchestra 水题     阅读数  学 Python 干什么 网友 我太难     阅读数 万  大学 四年 自学 走来 私藏 实用工具 学习 网站 贡献     阅读数  万  中国 程序员 青春 饭     阅读数  万  超全 Python 图像处理 讲解 多图 预警     阅读数 万  猝死 程序员 不见 产品 经理 猝死     阅读数  万  毕业 年 问遍 身边 大佬 总结 学习 方法     阅读数  万  推荐  堪称 神器 学习 网站     阅读数  万  强烈推荐  程序员 必读 书     阅读数 万  说 程序员 做外 包 没前途     阅读数  万  柏林 艺术家 行为艺术 骇 一次 谷歌 地图     阅读数   B 站上 学习 资源     阅读数  万  新手 程序员 一点 学习 建议     阅读数   新来 技术 总监 禁止 使用 Lombok     阅读数 万  字节 跳动 技术 架构     阅读数 万  三线 城市 工作 爽     阅读数 万  插件 太强 Chrome 必装 尤其 程序员     阅读数 万  抱歉 觉得 程序员 副业 赚钱 不靠 谱     阅读数 万  程序员 GitHub 项目 快 薅 羊毛     阅读数 万  删库 一定 跑 路     阅读数 万  金三银 四 敢不敢 试     阅读数   程序员 删库 跑 路     阅读数 万  跳槽 应届 毕业生     阅读数 万  学懂 数据结构 导图 发现 我错     阅读数 万  String s new String a 产生 几个 对象     阅读数 万  技术 大佬 写 switch 语句 太 老土     阅读数 万  当年 非典 SARS 真的 战胜     阅读数   学历 低 无法 胜任 工作 大佬 告诉 应该 做     阅读数 万  黑客 斗争 天     阅读数 万  讲 程序员 副业 月 赚 三万 真实 故事    """)

