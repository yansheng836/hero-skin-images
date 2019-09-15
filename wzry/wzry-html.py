# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: wzry.py
@time: 2019/9/15
"""
# 爬取王者荣耀的英雄皮肤图片

from urllib import request
from bs4 import BeautifulSoup
import os
import requests
from hero import Hero
from hero import HeroLink
import re

def mkdirs(path):
    """
    辅助函数：创建文件夹
    :param path: 文件夹名
    :return:
    """
    # 去除首末的空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # replace方法默认替换所有匹配项
    path = path.replace(":", "-").replace("?", "-").replace("|", "-")
    path = path.replace("<", "'").replace(">", "'").replace("\"", "'")

    # 判断路径是否存在，存在True，不存在False
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录，这里使用创建多重目录的函数
        os.makedirs(path)
        print('文件夹\'' + path + '\'创建成功！')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('文件夹\'' + path + '\'目录已存在！')
        return False


def getHeroUrl(url):
    """
    爬取每个英雄的英雄主页的网址
    :param url: 所有英雄的列表的主页，英雄资料列表页：https://pvp.qq.com/web201605/herolist.shtml
    :return:[英雄名：该英雄主页网址]
    """
    # 模拟真实浏览器进行访问
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode("gbk")  # 因为网页编码为gbk,使用gbk进行解码

    # 将获取的内容转换为BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(page_info, 'html.parser')
    soup.prettify()
    # 用选择器查找对应元素
    ul = soup.find('ul', class_="herolist clearfix")
    list = ul.find_all('li')
    # 拼接该英雄主页网址
    prefix = 'https://pvp.qq.com/web201605/'  # herodetail/518.shtml
    # 定义一个字典hero_url_dict{hero_name：url}
    hero_url_dict = {}
    hero_link_list = []
    for li in list:
        a = li.a
        hero_name = a.text
        suffix_url = a['href']  # 取得a标签的href的属性值
        hero_url_dict[hero_name] = prefix + suffix_url
        url = prefix + suffix_url

        # 获取id
        id = re.findall('\d+', a['href'])
        hero_link = HeroLink(id,hero_name,url)
        hero_link_list.append(hero_link)

    # 遍历
    # for dict in hero_url_dict:
    #     print(dict, hero_url_dict[dict])

    for herolink in hero_link_list:
        print(herolink.__str__())

    return hero_url_dict


def getSkins(url):
    """
    爬取每个英雄的皮肤的网址
    :param url: 某个英雄主页的网址
    :return:该英雄的皮肤名列表
    """
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64; x64) '
                      'AppleWebKit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode("gbk")
    # 将获取的内容转换为BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(page_info, 'html.parser')
    soup.prettify()
    # 用选择器查找对应元素
    ul = soup.find('ul', class_="pic-pf-list pic-pf-list3")
    # 取到皮肤名列表
    skin_string = ul['data-imgname']
    # print(ul)
    # print(skin_string)

    skin_list = skin_string.split('|')  # 注意这里是有顺序的
    # 打印皮肤列表
    # for skin in skin_list:
    #     print(skin)

    return skin_list


def downloadImages(hero_skin_list_dict):
    """
    主要的函数：获取王者荣耀图片信息，下载图片
    :param hero_skin_list_dict: 字典{英雄名：皮肤名列表}
    :return:
    """
    # 定义变量
    prefix_url1 = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/'
    prefix_url2 = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
    suffix_url = '.jpg'
    smallskin = '-smallskin-'
    mobileskin = '-mobileskin-'
    bigskin = '-bigskin-'

    phone_smallskin_dirpath = 'phone-smallskin-images'
    phone_mobileskin_dirpath = 'phone-mobileskin-images'
    phone_bigskin_dirpath = 'phone-bigskin-images'
    wallpaper_mobileskin_dirpath = 'wallpaper-mobileskin-images'
    wallpaper_bigskin_dirpath = 'wallpaper-bigskin-images'
    # 创建目录
    mkdirs(phone_smallskin_dirpath)
    mkdirs(phone_mobileskin_dirpath)
    mkdirs(phone_bigskin_dirpath)
    mkdirs(wallpaper_mobileskin_dirpath)
    mkdirs(wallpaper_bigskin_dirpath)

    for hero_name in hero_skin_list_dict:
        skin_list = hero_skin_list_dict[hero_name]
        # print(hero_name, " ",skin_list)

        # 拼接网址
        for skin in skin_list:
            # 获取下标，作为英雄皮肤数量
            index = skin_list.index(skin) + 1
            # skin_name_lists.index(skin_name_list)为列表的下标
            # https://game.gtimg.cn/images/yxzj/img201606/heroimg/ + 105 + '/ '+ 105 + '-smallskin-' + 1 + '.jpg'
            # 类型1
            mid_url = '%d' % id + '/' + '%d' % id
            phone_smallskin_url = prefix_url1 + mid_url + smallskin + '%d' % index + suffix_url
            phone_mobileskin_url = prefix_url1 + mid_url + mobileskin + '%d' % index + suffix_url
            phone_bigskin_url = prefix_url1 + mid_url + bigskin + '%d' % index + suffix_url
            # 类型2
            wallpaper_mobileskin_url = prefix_url2 + mid_url + mobileskin + '%d' % index + suffix_url
            wallpaper_bigskin_url = prefix_url2 + mid_url + bigskin + '%d' % index + suffix_url

            # 为方便起见，将对于类型的图片的文件夹和图片url组成 一对字典：
            url_dict = {
                phone_smallskin_dirpath: phone_smallskin_url,
                phone_mobileskin_dirpath: phone_mobileskin_url,
                phone_bigskin_dirpath: phone_bigskin_url,
                wallpaper_mobileskin_dirpath: wallpaper_mobileskin_url,
                wallpaper_bigskin_dirpath: wallpaper_bigskin_url,
            }
            # 遍历字典，取出对应键值，键：图片保存的目录，值：图片网址
            for dirpath in url_dict:
                # 定义保存到本地的图片名称，如：廉颇-1-正义爆轰.jpg
                image_path = dirpath + '/%s-%d-%s.jpg' % (cname, index, skin)
                # print("图片文件名：" + image_path)
                # 将判断放到前面，进行优化
                # 判断文件（图片）是否存在，如果存在就不重复下载，不存在就下载
                if os.path.exists(image_path):
                    print(' ' + image_path + '图片已存在！')
                    continue

                # 获取图片的网址，如果返回状态码为200，下载图片
                img_url = url_dict[dirpath]
                if requests.get(img_url).status_code == 200:
                    print('图片地址：' + img_url)
                    img = requests.get(img_url)

                    # 以二进制形式写文件（下载图片）
                    with open(image_path, 'wb') as f:
                        # f.write(img.content)  # 写入图片的二进制数据
                        print(' ' + image_path + '下载成功！')

        # 测试时，只下载一个英雄的皮肤图片；如需下载所有英雄的皮肤图片，请注释下面的break
        break


if __name__ == '__main__':
    # 英雄资料列表页
    home_url = 'https://pvp.qq.com/web201605/herolist.shtml'
    hero_url_dict = getHeroUrl(home_url)

    # 定义一个字典：hero_skin_list_dict{hero_name：skin_list}英雄名：皮肤列表
    hero_skin_list_dict = {}
    for hero_name in hero_url_dict:
        url = hero_url_dict[hero_name]
        skin_list = getSkins(url)
        # print(hero_name,end=":")
        # print(skin_list)

        # 将数据添加到字典中
        # hero_skin_list_dict[hero_name] = skin_list

        # 测试
        # break
    # 遍历
    # for hero_name in hero_skin_list_dict:
    #     print(hero_name, " ", hero_skin_list_dict[hero_name])

    # 下载图片
    # downloadImages(hero_skin_list_dict)
    # print('\n**王者荣耀全部英雄皮肤图片已下载成功**')