#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
if __name__ == "__main__":
    url='http://www.weather.com.cn/weather1d/101280101.shtml'
    jieguo=requests.get(url=url)
    #jieguoshuju=jieguo.text
    text = jieguo.content.decode('utf-8')
    print(text)
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(text)
    print('finished')

    pass