# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: wzry.py
@time: 2019/9/14
"""
# 爬取王者荣耀的英雄皮肤图片
import requests
import json
import os


def mkdirs(path):
    """
    辅助函数：创建文件夹
    """
    # 去除首末的空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    '''
    windows下文件名中不能含有：\ / : * ? " < > | 英文的这些字符 ，这里使用"'"、"-"进行替换。
    :?| 用-替换
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
        # 判断该英雄是否有skin_name属性（新英雄可能会没有），有就取值，没有就直接将列表置为空
        skin_name_lists = []
        if 'skin_name' in i.keys():
            skin_name = i['skin_name']  # 皮肤名
            skin_name_lists = skin_name.split('|')  # 把字符串变成列表，用|做分隔符
            # 记录英雄的title和skin_name的第一个属性不一样的英雄的id
            diff_ids = [109, 113, 176]
            if id in diff_ids:
                skins_lists = [title] + skin_name_lists[1:]
            else:
                skins_lists = [title] + skin_name_lists
        else:
            skins_lists = [title]
        # 将title 和skin_name_lists合并为列表，然后转为集合，自动去重,
        # 同时保证顺序不变，因为需要设置第一个为伴生皮肤
        skins_set_lists = list(set(skins_lists))
        skins_set_lists.sort(key=skins_lists.index)

        # 拼接网址
        for skin in skins_set_lists:
            # 获取下标，作为英雄皮肤数量
            index = skins_set_lists.index(skin) + 1
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
                        f.write(img.content)  # 写入图片的二进制数据
                        print(' ' + image_path + '下载成功！')

        # 测试时，只下载一个英雄的皮肤图片；如需下载所有英雄的皮肤图片，请注释下面的break
        break


if __name__ == '__main__':
    downloadImages()
    print('\n**王者荣耀全部英雄皮肤图片已下载成功**')
