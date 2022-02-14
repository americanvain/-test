#!usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import json

if __name__=="__main__":
    url='https://movie.douban.com/j/chart/top_list'
#    param={
 #       'type': '5',
#        'interval_id': '100:90',
 #       'action': '',               
  #      'start': '20',
   #     'limit': '20',
#    }
    param={
        'op':'兰州'
    }
    header={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    }  
    response = requests.get(url=url,params=param,headers=header)
    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')

    json.dump(list_data,fp,ensure_ascii=False)
    print('done')
    pass