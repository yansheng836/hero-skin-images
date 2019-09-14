# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: wzry.py
@time: 2019/9/14
"""
# 爬取王者荣耀的英雄皮肤图片
import requests
import json

def mkdirs(path):
    """
    辅助函数：创建文件夹
    """
    # 引入模块
    import os
    # 去除首末的空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    '''
    windows下文件名中不能含有：\ / : * ? " < > | 英文的这些字符 ，这里使用"'"、"-"进行替换。
    \/:?| 用-替换
    "<> 用'替换
    '''
    # 对于文件夹，有没有.好像都是同一个文件
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

def downloadImages():
    """
    主要的函数：获取王者荣耀图片信息，下载图片
    """
    '''
    1.按照分析，创建对应文件夹
    1.1.https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-smallskin-1.jpg
        phone-smallskin-images 头像
        phone-mobileskin-images 小屏手机图片
        phone-bigskin-images 大屏手机图片

    1.2.https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-mobileskin-1.jpg
       wallpaper-mobileskin-images 手机壁纸
       wallpaper-bigskin-images 电脑壁纸

    1.3. 观察url变化情况
    类型1：
    李白的第二个皮肤：https://game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-bigskin-2.jpg
    孙悟空的第二个皮肤：https://game.gtimg.cn/images/yxzj/img201606/heroimg/167/167-bigskin-2.jpg
    
    类型2：
    https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-mobileskin-1.jpg
    
    不同之处：131/131-bigskin-2
    '''
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

    # 2.获取英雄列表的json数据
    json_url = 'https://pvp.qq.com/web201605/js/herolist.json'  # 英雄的列表信息
    r = requests.get(json_url).text  # json数据--字符串
    # print(r)
    result = json.loads(r)  # 把字符串转换成字典，这里是由88个字典组成的list
    print('王者荣耀的英雄个数：%d' % len(result))  # 王者荣耀的英雄个数：88

    # 循环读取json数据，获得英雄对应数据，拼接图片url，下载图片
    for i in result:
        id = i['ename']  # 英雄id
        cname = i['cname']  # 英雄名
        title = i['title']  # 默认皮肤，即第一个皮肤
        skin_name = i['skin_name']  # 皮肤名
        # print('id:%s,cname:%s,title:%s,skin_name:%s'%(id,cname,title,skin_name))
        skin_name_lists = skin_name.split('|')  # 把字符串编程列表，用|做分隔符
        # print(skin_name_lists)
        # print(len(skin_name_lists))
        # for skin_name_list in skin_name_lists:  # 打印每一个list中的元素
        # print(skin_name_list)

        # print(type(id))
        # 拼接网址
        for skin_name_list in skin_name_lists:
            # skin_name_lists.index(skin_name_list)为列表的下标
            # https://game.gtimg.cn/images/yxzj/img201606/heroimg/ + 105 + '/ '+ 105 + '-smallskin-' + 1 + '.jpg'
            # 类型1
            phone_smallskin_url = prefix_url1 + '%d' % id + '/' + '%d' % id + smallskin + '%d' % (
                    skin_name_lists.index(skin_name_list) + 1) + suffix_url
            phone_mobileskin_url = prefix_url1 + '%d' % id + '/' + '%d' % id + mobileskin + '%d' % (
                    skin_name_lists.index(skin_name_list) + 1) + suffix_url
            phone_bigskin_url = prefix_url1 + '%d' % id + '/' + '%d' % id + bigskin + '%d' % (
                    skin_name_lists.index(skin_name_list) + 1) + suffix_url
            # 类型2
            wallpaper_mobileskin_url = prefix_url2 + '%d' % id + '/' + '%d' % id + mobileskin + '%d' % (
                    skin_name_lists.index(skin_name_list) + 1) + suffix_url
            wallpaper_bigskin_url = prefix_url2 + '%d' % id + '/' + '%d' % id + bigskin + '%d' % (
                    skin_name_lists.index(skin_name_list) + 1) + suffix_url
            print('图片地址：' + phone_smallskin_url)
            print('图片地址：' + phone_mobileskin_url)
            print('图片地址：' + phone_bigskin_url)
            print('图片地址：' + wallpaper_mobileskin_url)
            print('图片地址：' + wallpaper_bigskin_url)

            # 如果返回状态码为200，下载图片
            if requests.get(phone_bigskin_url).status_code == 200:
                img = requests.get(phone_bigskin_url)
                # 定义保存到本地的图片名称，如：廉颇-1-正义爆轰.jpg
                phone_bigskin_path = phone_bigskin_dirpath+'/%s-%d-%s.jpg' % (
                    cname, (skin_name_lists.index(skin_name_list) + 1), skin_name_list)

                # print("图片文件名：" + phone_bigskin_path)
                with open(phone_bigskin_path, 'wb') as f:
                    f.write(img.content)#写入图片的二进制数据
                    print('  %s下载成功！'%(phone_bigskin_path))

        # 测试时，只下载一个英雄的皮肤图片
        break


if __name__ == '__main__':
    downloadImages()
    print('\n**王者荣耀全部英雄皮肤图片已下载成功**')
