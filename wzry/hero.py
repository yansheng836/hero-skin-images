# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: hero.py
@time: 2019/9/15
"""


class HeroLink:
    """
    英雄资料主页的英雄信息：https://pvp.qq.com/web201605/herolist.shtml
    """

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def __str__(self):
        return 'HeroLink:id：%d, name: %s, url: %s' % (self.id, self.name, self.name)


class Hero:
    """
    英雄资料主页的英雄信息：https://pvp.qq.com/web201605/herolist.shtml
    """

    def __init__(self, name, id, skin_list):
        self.name = name
        self.id = id
        self.skin_list = skin_list


class HeroSkin:
    """
    某个英雄的详细信息，如马超：https://pvp.qq.com/web201605/herodetail/522.shtml
    """

    # 定义键值就可以了？skin(skin_name:skin_url)
    def __init__(self, url):
        self.url = url
