#!-*-coding:utf-8 -*-
'''
@author: yansheng
@file: 爬虫-wzry.py
@time: 2019/1/15 16:43
'''
#爬取王者荣耀的英雄皮肤
import requests
import re
import json

url = 'https://pvp.qq.com/web201605/js/herolist.json'  #英雄的列表信息
r = requests.get(url).text  #json数据--字符串
# print(r)
result = json.loads(r)      #把字符串转换成字典，这里是由88个字典组成的list
print('王者荣耀的英雄个数：%d'%len(result))       #王者荣耀的英雄个数：88

#李白的第二个皮肤：https://game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-bigskin-2.jpg
#孙悟空的第二个皮肤：https://game.gtimg.cn/images/yxzj/img201606/heroimg/167/167-bigskin-6.jpg
start_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/'

for i in result:
    id  = i['ename']            #英雄id
    cname = i['cname']          #英雄名
    title = i['title']          #默认皮肤，即第一个皮肤
    skin_name = i['skin_name']  #皮肤名
    #print('id:%s,cname:%s,title:%s,skin_name:%s'%(id,cname,title,skin_name))
    skin_name_lists = skin_name.split('|') #把字符串编程列表，用|做分隔符
    # print(skin_name_lists)
    # print(len(skin_name_lists))
    # for skin_name_list in skin_name_lists:  # 打印每一个list中的元素
    # print(skin_name_list)

    #print(type(id))
    #拼接网址
    for skin_name_list in skin_name_lists:
        # skin_name_lists.index(skin_name_list)为列表的下标
        result_url = start_url+'%d'%id+'/'+'%d'%id+'-bigskin-'+'%d'%(skin_name_lists.index(skin_name_list)+1)+'.jpg'
        print('图片地址：'+result_url)

        #下载图片
        if requests.get(result_url).status_code == 200:
            img = requests.get(result_url)
            with open('wzry-hero-skin/%s-%d-%s.jpg'%(cname,(skin_name_lists.index(skin_name_list)+1),skin_name_list),'wb') as f:
                f.write(img.content)#写入图片的二进制数据
                print('wzry-hero-skin/%s-%d-%s.jpg 下载成功！'%(cname,(skin_name_lists.index(skin_name_list)+1),skin_name_list))



