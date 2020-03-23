import requests
from Settings import HEADERS
import urllib3
from bs4 import BeautifulSoup
import re
import chardet

url = "https://new.qq.com/rain/a/20200309A03NXV00"

urllib3.disable_warnings()
html = requests.get(url, headers=HEADERS, verify=False).content.decode('utf-8')

# re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I) #Script
# re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)  #style
# re_h=re.compile('</?\w+[^>]*>')  #匹配HTML标签
# re_comment=re.compile('<!--[^>]*-->')#HTML注释

html = re.sub('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', "", html)  # Script
html = re.sub('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', "", html)    # style
html = re.sub('<!D.*? html>', "", html)                             # html头
html = re.sub('</?\w+[^>]*>', "", html)                             # HTML标签
html = re.sub('<!--.*?-->', "", html)                               # HTML注释
html = re.sub('[\t]*', "", html)

print(html)

fh = open(r'E:\c++\毕业设计开发日志\06.文本数据集\a.txt', 'w+', encoding='utf-8')
fh.write(html)
fh.close()
