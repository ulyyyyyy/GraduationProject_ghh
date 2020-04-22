13861792669

from requests import get
from Settings import HEADERS
import json
from data_cleaning.Extractor import Extractor
from data_cleaning.content_clean import clean_content

if __name__ == '__main__':
    api = "https://www.huomao.com/channels/channelnew.json?page=1&game_url_rule=dota2"
    res = get(api, headers=HEADERS)
    res.encoding = 'utf-8'
    print(res.text)