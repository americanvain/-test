#!/usr/bin/env python
# -*- utf-8 -*-
from bs4 import BeautifulSoup
import requests
from lxml import etree

if __name__ == "__main__":
    # tree = etree.parse('58_original.html')
    # print(etree.tostring(tree))
    # # /html/body/div/div/div/section/section[3]/section[1]/section[2]/div[1]/a/div[2]/div[1]/div[1]/h3
    # r = tree.xpath('/html/head')
    # print(r)

    fp = open('58_original.html','r',encoding='utf-8')
    result = fp.read()
    tree = etree.HTML(result)
    r_list = tree.xpath('/html/body/div/div/div/section/section[3]/section[1]/section[2]/div')
    for r in r_list:
        title = r.xpath('./a/div[@class="property-content"]//h3[@class="property-content-title-name"]/@title')
        print(title[0])
        pass
    # print(etree.tostring(r[0]))
    # fp = open('./58_original.html','r',encoding='utf-8')
    # soup = BeautifulSoup(fp,'lxml')
    # r = soup.select('.property-content-title-name')
    # for i in r:
    #     print(i.text)
    #     pass

    # some_xml_data = "<root>data</root>"

    # root = etree.fromstring(some_xml_data)
    # print(root.tag)
    # print(etree.tostring(root))

    pass
