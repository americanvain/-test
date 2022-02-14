#!usr/bin/env python
#-*- coding:utf-8 -*-

import json
import requests

if __name__ =="__main__":

    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    header={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
    param={
        'cname': '',
        'pid': '',
        'keyword': '兰州',
        'pageIndex': '1',
        'pageSize': '10',
    }
    r=requests.post(url=url,headers=header,params=param)
    print(r.text)
    print(r.status_code)
    with open('kfc_lanzhou.txt','w',encoding='utf-8') as fp:
        fp.write(r.text)
    print('finished')

    pass