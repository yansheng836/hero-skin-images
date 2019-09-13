#!-*-coding:utf-8 -*-
'''
@author: yansheng
@file: 爬虫-lol.py
@time: 2019/1/15 14:51
'''
#爬取lol的英雄皮肤的图片

#1.尝试保存一张图片
import requests
import re
import json
# url = 'https://ossweb-img.qq.com/images/lol/web201310/skin/big266001.jpg'
# r = requests.get(url)
# with open('1.jpg','wb') as f:
#     f.write(r.content)

# 2.一步步分解（url）：
#（1.不变的     2.英雄ID      3.皮肤序号）
# https://ossweb-img.qq.com/images/lol/web201310/skin/big266001.jpg
start_url = 'https://ossweb-img.qq.com/images/lol/web201310/skin/big'
# 1.1英雄的所有ID
url = 'https://lol.qq.com/biz/hero/champion.js'
r = requests.get(url).text
# print(r)
#用正则提取字符串的数据
ret = re.search('"keys":(.*?),"data"',r)
id_list = ret.group(1)#1表是提取的第一个小括号的值
# print(id_list)            #
# print(type(id_list))    #字符串 json数据，要变成字典

id_dict =  json.loads(id_list)  #把字符串转换成一个字典
# print(id_dict)
# print(type(id_dict))

for i,j in id_dict.items():
    # print(i,j)
    id = i
    name = j
    # 2.拼接所有皮肤地址
    for k in range(2):#这里可设置的大一点
        result_url = start_url +id + '%03d'%k + '.jpg'

        # 3.保存图片
        if requests.get(result_url).status_code == 200:
            img = requests.get(result_url)
            with open('lol-hero-skin/%s%d.jpg' % (name,k),'wb') as f:
                f.write(img.content)  #写入图片的二进制数据
                print('下载 lol-hero-skin/%s%d.jpg 成功'% (name,k))
