import requests, re
from Settings import HEADERS

res = requests.get("https://s.weibo.com/top/summary?cate=realtimehot", headers=HEADERS)
res2 = requests.get("https://s.weibo.com/top/summary?cate=socialevent", headers=HEADERS)
data = res.text
data2 = res2.text
re_l = 'target="_blank">#*(.*?)#*</a>'
words = re.findall(re_l, data)
words += re.findall(re_l, data2)
for word in words:
    with open("C:/Users/叫乌鸦的少年怪/Desktop/words.txt", 'a+', encoding='utf-8') as txt:
        txt.write(word + '\n')