#! usr/bin/env python3
#-*- coding:utf-8 -*-#

from bs4 import BeautifulSoup
import lxml
import requests
if __name__ == "__main__":
    url1='https://www.shicimingju.com/book/hongloumeng.html'
    header={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
    html1=requests.get(url=url1,headers=header)
    html1.encoding='utf-8'
    html1_text=html1.text
    soup = BeautifulSoup(html1_text,'lxml')
    li_html1=soup.find('div',class_="book-mulu").find_all('li')
    fp = open('./hongloumeng.txt','w',encoding='utf-8')
    for li in li_html1:
        title_text=li.string
        title_url='http://www.shicimingju.com'+li.a['href']
        html2=requests.get(url=title_url,headers=header)
        html2.encoding='utf-8'
        soup2=BeautifulSoup(html2.text,'lxml')
        div_tag=soup2.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title_text+':'+content+'\n')
        print(title_text,'爬取成功')

    pass