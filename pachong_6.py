#!usr/bin/env python3
import requests
import json

if __name__ == "__main__":
    headers={
        'User-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
    }
    url1="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    data1={
	'on': 'true',
	'page': '1',
	'pageSize': '15',
	'productName': '',
	'conditionType': '1',
	'applyname': '',
	'applysn': ''
    }   
    jieguo1 = requests.post(url=url1,data=data1,headers=headers).json()
    jieguo_id=[]
    all_data_list=[]
    for dic in jieguo1['list']:
        jieguo_id.append(dic['ID'])

    print(jieguo_id)
    url2='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

    for id in jieguo_id:
        data2={
        'id':id
        }
        jieguo2 = requests.post(url=url2,data=data2,headers=headers).json()
        all_data_list.append(jieguo2)
        fp=open('./05_alldatalist','w',encoding='utf-8')
        json.dump(all_data_list,fp=fp,ensure_ascii=False)
        print('over')
    pass