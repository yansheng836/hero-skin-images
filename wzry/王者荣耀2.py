#!-*-coding:utf-8 -*-
'''
@author: yansheng
@file: 王者荣耀2.py
@time: 2019/1/27 15:04
'''
import requests
from bs4 import BeautifulSoup
url = 'https://lol.qq.com/data/info-heros.shtml'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
response = requests.get(url= url,headers = headers)
soup = BeautifulSoup(response.text,'lxml')
print(soup)
# li_list = soup.select('li a')
# # print(li_list)
# for li in li_list:
#     print(li)

