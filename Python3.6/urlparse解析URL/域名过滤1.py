# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 10:15
# @Author  : play4fun
# @File    : 域名过滤1.py
# @Software: PyCharm

"""
域名过滤1.py:
"""
import traceback
import urllib
from urllib.parse import urlparse

# 淘宝客推广链接
url = 'https://detail.tmall.com/item.htm?id=561067099846&ali_trackid=2:mm_18989874_43894087_376356913:1525658813_216_155664132&pvid=10_182.48.115.66_547_1525658757001'
pas: urllib.parse.ParseResult = urlparse(url)

domain_filter_list = ['taobao.com', 'tmall.com']

# 获取主域名
main_domain = '.'.join(pas.hostname.split('.')[-2:])
if main_domain in domain_filter_list:
    print('域名过滤', True)


def domain_filter(url, filter_list):
    try:
        pas: urllib.parse.ParseResult = urlparse(url)
        main_domain = '.'.join(pas.hostname.split('.')[-2:])
        return main_domain in filter_list
    except Exception as e:
        print(traceback.format_exc())
        return False

url2='https://item.taobao.com/item.htm?spm=a219t.7900221/10.1998910419.d5d3d3cdd.310875a5ZRaI7x&id=567973056473'
url3='http://localhost:51009/d159069e6fb6a56a2ab22261b20996ab/?utm_campaign=startup&utm_content=&utm_medium=lantern&utm_source=darwin'
filt=domain_filter(url3,domain_filter_list)
print('过滤结果',filt)
