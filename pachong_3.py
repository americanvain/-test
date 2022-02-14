#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json
if __name__=="__main__":

    post_url='https://fanyi.baidu.com/sug'
    word = input('enter a word')
    data={
        'kw':word
    }
    headers={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    dic_obj=response.json()
    print(dic_obj)
    filename = word +'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)


    print('finished')
    pass

