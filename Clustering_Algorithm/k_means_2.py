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
    Kmeans.keams_predict(r'C:\Users\叫乌鸦的少年怪\Desktop\content.txt')
    # Kmeans.get_labels()
    # Kmeans.single_content_analyse("""版权 声明 本文 博主 原创 文章 CC  BY NC SA 版权 协议 转载 请 附上 原文 出处 链接 声明  本文 链接 https blog csdn net qq  article details   文章 目录 PanDownload 简介 PanDownload 作者 抓 观点 百度网 盘 简单 nas 成本计算 总结  PanDownload 简介  PanDownload 说 简单 点 利用 多线程 技术 避开 百度 限速 免费 用户 体验 百度网 盘 高速下载 技术 层面 PanDownload 作者 在我看来 大佬 技术 当前 仰望  观点 PanDownload 用户 享受 收费 用户 待遇 用户 获 利 使用 过此 工具 说 现在 常用 几个 网盘 加速 工具 加速 工具 比冲 会员 官方 下载 快  推测 百度 会员 一定 限速 每个 传输 连接 带宽 上线 多线程 伪造 多个 用户 下载 实现 提速 创造 多个 连接 下载速度 上限  下载 东西 普通用户 水管 超级 会员 水管 多线程 多个 水管 水管 数量 够 完全 做到 比大 水管 速度 快  PanDownload 作者 抓 观点  PanDownload 作者 感到 可惜 个人感觉 百度网 盘 做 理解 知道 大多数 PanDownload 用户 无法 接受 事实 PanDownload 提供 免费 高速下载 服务 被告 有罪 要求 巨额 赔偿 PanDownload 公平 气 撒 百度网 盘 认为 百度网 盘 错 觉得 行为 理智  PanDownload 作者 被告 百度 官方 解释 PanDownload 致使 损失 千万 官方 如果说 直接 损失 我会 质疑 严重 夸大 行为  PanDownload 作者 做 底层 云盘 服务 非 百度 云盘 基础 做 破解 服务 出现 今天 事情 PanDownload 作者 做 觉得 究其原因 无非 两个 成本 技术 几年 前 一大堆 主流 厂商 顶住 网盘 成本 仅仅 开发者  假设 开发者 软件 收费 服务 破解 公开 网上 供给 所有人 免费 使用 作何 感想 挣 挣钱 无所谓 百度 可不是 圣人 一家 盈利 目的 公司 光彩 百度 搜索 说 盈利 手段 云盘 这种 正规 手段 不去 维护  百度 一款 盈利性 产品 广告 会员 进行 盈利  这是 当前 会员 原价 活动 价钱 降低 去年 周年  价格 购入  粗略 来算 一下 百度网 盘 成本  服务器 集群 百度 山西 阳泉 数据中心  万个 存储器 存储  万 TB 数据 最少 万台 服务器 占据 位置 足球场 服务器 集群 要求 无菌 无尘 低温 环境 大型 服务器 集群 建立 封闭 空调 室内 一次性 成本 外 持续 运行 需要 巨额 电费 网费 不同于 家用 用户 需要 三大 运营商 通网 每年 成本 最少 亿来 计算 一套 成熟 服务器 集群 两套 备份 一套 备份 一套 异地 备份 以防 天灾人祸 上述 计算 人力 成本 服务 场地 搭建 服务端 客服 端 程序 李彦宏 一人 完成 来算  巨额 成本 来算  一年 超级 会员 真的 接受 百度 一家 盈利性 企业 来算 想 仅仅 回 需要 进行 盈利 觉得 盈利 这件 事 光彩 互联网 企业 应该 产品 免费 只能 说 做梦  接受 百度 需要 限速 迫使 用户 充值 会员 进行 盈利 手段 选择 搭建 nas 使用 网盘 服务 当前 蓝奏云 比较 受欢迎 好像 免费 用户 只能 上传 一百 MB 单个 文件 会员 上传 更大 文件 皮皮 盘 非会员 同样 下载 限速 会员 百度 便宜 选择权 国内外 网盘 厂商 家 要求 哪家  简单 nas 成本计算  先以 普通 程序员 视角 粗略 计算 使用 nas 所需 成本  nas 发烧友 高 玩 技术水平 一台 报废 主机 改为 nas 当前 实力 相信 大部分 成本 计算 类似 这种 情况  买 nas 主机 二手 咸鱼 粗略 查看 两百 T 硬盘  元 东西 不算   来算 硬件 价钱  解决 问题 关键 问题 网络 地区 个人用户 无法 运营商 索取 固定 ip 需要 开通 专用线路 获取 固定 ip 专用线路 月 收费 千元 方式 反向 代理 需要 一定 技术实力 购买 服务器 实现 反向 代理 国内 比较稳定 服务器 厂商 兆 宽带 便宜 年份 解决 四百多 价位 难 找到 大部分 新 用户  搭建 nas 学习 成本 相对 高  根据上述 相比 觉得 百度网 盘 做 过分 错 过分 限速 过低 PanDownload 作者 先 警告 警告 没 了解 听 采取行动 会员 收费 理解 百度 做法 希望 PanDownload 不停 喷击 百度网 盘 意义    说 百度 想想 多人 PanDownload 喷 百度 提 百度 说明 一下 PanDownload 关停 导致 利益 受损 免费 使用 会员 体验 服务 觉得 使用 破解版 当成 自豪 事情 感觉 自卑 开发者 辛苦 开发 软件 找到 破解版 免费 使用 里面 感觉 自豪 找到 破解版 免费 使用 掏钱 服务 白嫖使 快乐 快乐 白 嫖 官方 正规渠道 白 嫖 得来 非 非法 破解 得来     文章 举报  O 寻觅 O  发布  篇 原创 文章 获赞  访问量 万  下载 地址 http pandownload com 小心 百度 封 ID 限速 风险 运行 exe 文件 登录 网盘 账户 即可 随心所欲 下载 百度网 盘 下载 完成 以后 发现 使用 网速  musicwHello  相信 网友 百度 云盘 爱 恨 爱 应为 免费 存储空间 百度 云盘 资源 丰富 需要 一键 转存 百度 云盘 空间 方便 恨 花钱 开通 超级 会员 下载速度 慢 本期 系统 部落  weixin  博客  ​ 提供 百度网 盘 软件 破解 版本 划掉 版本 资源 教程 软件 已经 描述 优点 破解版 百度 云 替代品 下载 限速 免费软件 PC 安卓 网页 版 提供 熊掌 百度 修改 相关  xmuli tech  最近 同学 反应 使用 百度网 盘 下载 Python 自学 视频 速度 慢 菜鸟 小白菌 搜遍 全网 找到 神器 度盘 PanDownload 下载 器 限速 下载 百度网 盘 里面 视频 百度网 盘 不容  l 博客  平时 使用 百度网 盘 下载 东西 时 通常 速度 很慢 现在 推荐 一款 百度网 盘 下载工具 下载 分享 链接 登录 网盘 下载 速度 百度 云快 倍 话 说 下面 图 PanDownloa  feengg 博客  写 前面 先说 题外话 最近 更文 这段 没人 发现 我断 更 抓 包 dbq 忙 填 埋下 坑 忙里偷闲 学回针 绣 缎面 绣 链 绣 针法 非 压迫 bulingbuling 真真  路 拾遗 博客  百度网 盘下 东西 真是 龟速 网上 查 一下 下载 软件 Pandownload 链接 http pandownload com 跳转 网页 选择 本地下载 解压 下载 压缩包 双击 打开 PanDownload  zj 博客  基本概念 Tampermonkey 油猴 Tampermonkey 插件 免费 浏览器 扩展 最为 流行 用户 脚本 管理器 拥有 适用 Chrome MicrosoftEdge Safari Opera  StarSky STZG  目前 满速 跑 下载 里面 最大 连接数 设置  登陆 百度 账号 粘贴 下载 文件 链接 提取 码 使用 PanDownload 下载 相信 pandownload 需要 最新 版本 私信  Laic Zhang 博客  没用 PanDownload 之前 百度网 盘 下载速度 k s 之后 每秒 M 安利 安装包 下载 地址 https download csdn net download qq   Android 之旅  知道 Pandownload 干嘛 简单 解释一下 Pandownload 百度网 盘 限速 下载 软件 官网 下载 pandownload 软件 http www p  linux 博客  工种 号 潮 软件 软件 介绍 PanDownload 一款 百度网 盘 高速 下载工具 国内 论坛 大神 制作 无需 会员 功能 即可 享受 高速下载 功能 提供 实用 功能 完全 百度 客户端 日常 使用 百度 云  weixin  博客  曾经 风靡 全网 知名 百度 百度网 盘 限速 下载工具 PanDownload 面对 百度网 盘 官方 精准 打击 面对 大量 封号 失去 普通用户 走上 低调 内容 vip 之路 百度 做 没能 阻挡 住 破解 不断 新  qq  博客  声明 PanDownload 注意 需要 登录 百度网 盘 账号 不用 担心 账号 IP 限速 方式 PanDownload 网页 版 进行 下载 PanDownload 网页 版 进行 下载 网址 www bai  Hern 宋兆恒  PanDownload 使用 场景 网速 够快 百度网 盘 下载速度 慢 穷 不想 开 会员 情况 简介 pojie 会员 制作 帮助 用户 快速 不受 速度限制 德 下载 网盘 文件 使用 简单 复制 网盘 地址  小仙 博客  软件 介绍 工种 号 下载 潮 软件 PanDownload 一款 百度网 盘 高速 下载工具 国内 论坛 大神 制作 无需 会员 功能 即可 享受 高速下载 功能 提供 实用 功能 完全 百度 客户端 日常 使用 百度  weixin  博客  这款 pandownload 直接 绕过 百度网 盘 进行 下载 服务 多线程 下载 直接 打开 操作 简单 打开 直接 下载 地址 pandownload 一款 下载 器 https blog   龙烨 专栏  感觉 全世界 营销 文都 推 Python 找 不到 工作 机构 站 推荐 工作 笔者 冷静 分析 多方 数据 想 说 超越 老牌 霸主 Java 过去 几年 间 Python 寄予厚望 事实  CSDN 学院  大学 四年 课本 课本 学习 特别 自学 善于 搜索 网上 资源 辅助 必要 下面 几年 私藏 资源 网站 贡献 主要 电子书 搜索 实用工具 在线视频  帅地  今年  误导 咨询 猎头 圈内 好友 年  岁 几位 老 程序员   舍 老脸 揭 伤疤   希望 帮助 记得 帮 点赞 目录 人生 一次 一次 伤害 猎头 界 真  启舰  文章 目录 Pillow 模块 讲解 Image 模块  打开 图片 显示 图片  创建 简单 图像  图像 混合 透明度 混合 遮罩 混合  图像 缩放 像素 缩放 尺寸 缩放   ZackSock 博客  相信 时不时 听到 程序员 猝死 消息 听 不到 产品 经理 猝死 消息 这是 先 百度搜 一下 程序员 猝死 出现  多万条 搜索 搜索 一下 产品 经理 猝死  万条 搜索 搜  曹银飞 专栏  每天 收到 读者 私信 问 二哥 推荐 学习 网站 最近 浮躁 手头 网站 看烦 想 看看 二哥 新鲜 货 今天 一早 做 恶梦 梦到 老板 辞退 说 公司 辞退 老  沉默 王二  遗憾 春节 注定 刻骨铭心 新型 冠状病毒 每个 神经 紧绷 武汉 白衣天使 尤其 值得 尊敬 窝 家里 程序员 外出 外出 社会 做出 最大 贡献 读者  沉默 王二  之前 做过 不到 月 外包  第一天 释放  年 剩 天 外包 公司 离职 谈谈 看法 定义 一下 前途 稳定 工作 环境 不错 收入 能够 项目 中 不断  dotNet 全栈 开发  一辆 装  部 智能手机 手 拉车 一位 柏林 艺术家 一条 空荡荡 街道 骇 一次 谷歌 地图 成功 虚拟 堵车 柏林 艺术家 Simon Weckert 最近 Google 地图 功能 代替 路障 禁  德国 IT 事  说起 B 站 九 眼里 宝藏 存在 放年 假宅 在家 时 一天 刷 小时 不在话下 更 别提 今年 跨 年 晚会 跪 完 最早 聚 B 站 追番 上面 刷 欧美 新歌 漂亮 小姐姐 舞蹈 视  九章 算法 博客  几年 经验 程序员 之前 发展 却是 一头雾水 知道 主流 技术 知道 工作 迎合 主流 技术 迎合 公司 发展 感触 两年 坚持 学习 迎合 公司 发展 前提 学  JAVA 圈 博客  学弟 一家 小型 互联网 公司 做 Java 后端 开发 最近 公司 新来 技术 总监 这位 技术 总监 技术细节 看重 公司 之后 推出 政策 定义 开发 规范 日志 规范 要求 统一  HollisChuang s Blog  字节 跳动 创立  年 月 目前 仅 年 时间 十几个 工程师 研发 上百人  余人 产品线 内涵 段子 今日 头条 今日 特卖 今日 电影 产品线 产品 背景 今日 头条 用户 提供 个性化 资讯 客  作 独立 连续 思考者  一名 程序员 青春年华  岁 回到 三线 城市 洛阳 工作 已经 年 有余 一不小心 暴露 实际 年龄 老 读者 知道 驻颜有术 上次 房子 业务员 肯定 地说 小哥 肯定 今年  沉默 王二  最近 看到 程序员 副业 赚钱 文章 出 点子 网上 找 项目 做 兼职 录制 课程 网上 平台 售卖 免费 推广 赚 广告费 写 付费 专栏 文章 寻找 漏洞 获取 赏金  码农 翻身  今天下午 朋友圈 看到 发 github 羊毛 一时 没 明白 怎么回事 百度 搜索 一下 原来 真有 回事 资源 主义 羊毛  刀刷 爆 朋友圈 知道 朋友圈 有没有 看到 类似 消息  dotNet 全栈 开发  工作 中 误删 数据 数据库 一定 需要 跑 路 未必 程序员 一定 学会 自救 神不知鬼不觉 数据 找回 mysql 数据库 中 知道 binlog 日志 记录 数据库 操作  平头 哥 技术 博文  Django 数据库 迁移 命令  报错 django db utils OperationalError  迁移 版本 报错 解决 ✧ ｡  ˊ ᗜ ˋ و ✧ ｡ Django 初体验  安装 汉化 win linux 子系统 win linux 子系统 启动 桌面 Windows Linux 子系统 安装 使用 自带 远程桌面 映射 出 Linux 子系统 OAO kali 篇  阅读数   数据库 MySQL 搭建 MySQL 数据库 cmd 连接 MySQL 常用 支持 MySQL 数据库 可视化 软件 包含 下载 地址 ~ ` 数据库 """)

