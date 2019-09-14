# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: testMakeDirs.py
@time: 2019/9/14
"""
import os

# dirpath = "./nihao";
# os.mkdir(dirpath);


def mkdirs(path):
    # 引入模块
    import os

    # 去除首末的空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    """
    windows下文件名中不能含有：\ / : * ? " < > | 英文的这些字符 ，这里使用"'"、"-"进行替换。
	\/:?| 用-替换
	"<> 用'替换
    """
    # 对于文件夹，有没有.好像都是同一个文件
    # replace方法默认替换所有匹配项
    path = path.replace(":","-").replace("?","-").replace("|","-")
    path = path.replace("<", "'").replace(">", "'").replace("\"", "'")

    # 判断路径是否存在，存在True，不存在False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录，这里使用创建多重目录的函数
        os.makedirs(path)
        print('文件夹\''+path + '\'创建成功！')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('文件夹\'' + path + '\'目录已存在！')
        return False

# 定义要创建的目录
mkpath = "./你好/23#|"
# 调用函数
mkdirs(mkpath)
