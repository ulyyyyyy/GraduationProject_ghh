import requests
from Settings import HEADERS
import json

# Csdn_api
csdn_apis = []
title = []
url = []

for i in range(6):
    csdn_api = f"https://blog.csdn.net/api/articles?type=more&category=python&shown_offset={i}"
    csdn_apis.append(csdn_api)

response = requests.get(csdn_apis[0], headers=HEADERS)
html = response.text
data_json = json.loads(html)
for article in data_json['articles']:
    title.append(article['title'])
    url.append(article['url'])

print(title)
print('====================================')
print(url)