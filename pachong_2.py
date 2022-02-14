#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
if __name__=="__main__":
    headers={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
    url='https://www.sogo.com/web'
    kw = input('enter a word')
    param={
        'query':kw
    }
    response=requests.get(url=url,params=param,headers=headers)

    page_text=response.text
    filename=kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'finished')
pass



