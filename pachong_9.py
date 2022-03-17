#!/usr/bin/env python
# -*- utf-8 -*-
import os
import requests
from lxml import etree
from bs4 import BeautifulSoup
if __name__ == "__main__":
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
    url1 = 'https://pic.netbian.com/4kmeinv/'

    response = requests.get(url=url1,headers=header)
    response.encoding='gbk'
    response = response.text
    soup = BeautifulSoup(response,'lxml')
    result = soup.prettify()
    
    tree =etree.HTML(result)
    r_list = tree.xpath('/html/body/div[2]/div/div[3]/ul/li')
    if not os.path.exists('.picLib'):
        os.mkdir('./picLibs')
    for r in r_list:
        src = r.xpath('./a/img/@src')[0]
        title = r.xpath('./a/img/@alt')[0]+'.jpg'
        # title = title.encode('iso-8859-1').decode('gbk')
        url = 'https://pic.netbian.com/'+str(src)
        # print(title,src)

        tupian = requests.get(url=url,headers=header).content
        tupianlujing = './picLibs/'+title
        with open(tupianlujing,'wb') as fp:
            fp.write(tupian)
            print(title,'finished')
        pass
    pass
