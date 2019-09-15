# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: testJson.py
@time: 2019/9/15
"""
import json

# 读取本地json数据
data = open("../json数据/herolist.json", encoding='utf-8')
result = json.load(data)  # 把字符串转换成字典，这里是由88个字典组成的list
print('王者荣耀的英雄个数：%d' % len(result))

count=0
for i in result:
    # print(i)
    id = i['ename']  # 英雄id
    cname = i['cname']  # 英雄名
    title = i['title']  # 默认皮肤，即第一个皮肤
    skin_name = i['skin_name']  # 皮肤名
    # print('id:%s,cname:%s,title:%s,skin_name:%s'%(id,cname,title,skin_name))
    skin_name_lists = skin_name.split('|')  # 把字符串变成列表，用|做分隔符

    # 方法1：将title 和skin_name_lists合并为列表，然后转为集合，自动去重
    skins_list = [title]+skin_name_lists
    skins_set1 = set(skins_list)

    # 方法2：先分别转换成集合，然后进行集合的“并”
    skin1 = set([title])
    skin2 = set(skin_name_lists)
    skins_set2 = skin1.union(skin2)

    # 方法3：将方法1的集合再转为list，同时保证顺序不变，因为需要设置第一个为伴生皮肤
    skins_set1_list = list(skins_set1)
    skins_set1_list.sort(key=skins_list.index)

    print(cname, end=':')
    for skin in skins_set1_list:

        print(skin, end=',')

    print()
    count=count+1
    if count>3:
        break
