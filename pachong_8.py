#!/usr/bin/env python
# -*- utf-8 -*-
from bs4 import BeautifulSoup
import requests
from lxml import etree

if __name__ == "__main__":
    headers ={
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    url = "https://gz.58.com/ershoufang/"
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    result = soup.prettify()
    # fp = open('58_original.html','w',encoding='utf-8')
    # fp.write(result)
    tree = etree.HTML(result)
    r_list = tree.xpath('/html/body/div/div/div/section/section[3]/section[1]/section[2]/div')
    fp = open('58_title.txt','w',encoding='utf-8')
    for r in r_list:
        title = r.xpath('./a/div[@class="property-content"]//h3[@class="property-content-title-name"]/@title')[0]
        print(title)
        fp.write(title+'\n')
        pass
    pass
