import re
from collections import Counter
import matplotlib.pyplot as plt

str = """[1 4 1 4 1 0 4 4 4 4 2 4 4 3 0 0 3 0 3 4 3 0 0 0 4 3 0 4 3 0 0 0 4 0 3 0 2
 4 0 2 4 2 4 0 2 0 2 2 3 0 0 0 3 3 0 2 3 0 2 2 4 3 2 3 2 2 3 2 2 3 2 2 3 0
 0 3 0 1 0 4 2 2 1 2 1 0 4 0 4 2 4 2 0 0 4 2 4 4 2 0 4 4 4 4 4 0 3 2 0 2 0
 4 2 4 2 2 4 2 3 3 4 2 2 2 2 4 2 4 2 0 2]"""
list2 = re.findall("\d", str)
result = Counter(list2)
print(list(result.values()))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(list(result), list(result.values()), width=0.4)
plt.xlabel('访问网页分类', fontsize=8)
plt.ylabel('访问次数', fontsize=8)
plt.title('上网行为分析图', fontsize=10)

for a, b in zip(list(result), list(result.values())):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

plt.show()

