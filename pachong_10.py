#! /usr/bin/env python
# -*- utf-8 -*-

from email import header
import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "https://www.aqistudy.cn/historydata/"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
}
response = requests.get(url=url,headers=header)
response.encoding = 'utf-8'
text = response.text

tree = etree.HTML(text)
r_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul')
fp = open('cit_list','w',encoding='utf-8')
for r in r_list:
    city_list = r.xpath('./div[2]/li')
    for city in city_list:
        city_text=city.xpath('./a/text()')[0]
        fp.write(city_text+'\n')
        pass
    pass