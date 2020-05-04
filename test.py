from data_cleaning.Extractor import Extractor
import re
from data_cleaning.content_clean import clean_content

ex = Extractor(threshold=30)
html = ex.getHtml('https://blog.csdn.net/freesum/article/details/7376006')
all_data = len(html)
content = ex.filter_tags(html)
text_data = len(content)
# print(content)
content = re.sub("\n", "", content)
# print(content)
per = "{:.2%}".format(text_data/all_data)

# print(f"总长度{all_data}， 文本长度{text_data}, 百分比{per}")

content = clean_content(content)
print(content)