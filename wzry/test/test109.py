# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: test109.py
@time: 2019/9/15
"""
import json

# 读取本地json数据
data = open("../json数据/herolist.json", encoding='utf-8')
result = json.load(data)  # 把字符串转换成字典，这里是由88个字典组成的list
print('王者荣耀的英雄个数：%d' % len(result))

count=0
for i in result:
    id = i['ename']  # 英雄id
    cname = i['cname']  # 英雄名
    title = i['title']  # 默认皮肤，即第一个皮肤
    # 判断该英雄是否有skin_name属性，有就取值，没有就直接将列表置为空
    if 'skin_name' in i.keys():
        # print(i)
        skin_name = i['skin_name']  # 皮肤名
        skin_name_lists = skin_name.split('|')  # 把字符串变成列表，用|做分隔符
        # 记录英雄的title和skin_name的第一个属性不一样的id
        diff_ids = [109, 113, 176]
        if id in diff_ids:
            skins_lists = [title] + skin_name_lists[1:]
        else:
            skins_lists = [title] + skin_name_lists
    else:
        skin_name_lists = []
        skins_lists = [title]

    skins_set_lists = list(set(skins_lists))
    skins_set_lists.sort(key=skins_lists.index)

    # 查看那些英雄的title和skin_name的第一个属性不一样
    # id = 109,113，176
    # if title != skin_name_lists[0]:
    #     print(i)
    #     print(skins_set_lists)
    #     # break
    print(i)
    for skin in skins_set_lists:
        print(skin,end=',')
    print()



