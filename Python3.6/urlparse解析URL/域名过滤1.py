# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 10:15
# @Author  : play4fun
# @File    : 域名过滤1.py
# @Software: PyCharm

"""
域名过滤1.py:
"""

import urllib
from urllib.parse import urlparse

#淘宝客推广链接
url='https://detail.tmall.com/item.htm?id=561067099846&ali_trackid=2:mm_18989874_43894087_376356913:1525658813_216_155664132&pvid=10_182.48.115.66_547_1525658757001'
pas:urllib.parse.ParseResult=urlparse(url)

domain_filter_list=['taobao.com','tmall.com']

#获取主域名
main_domain='.'.join(pas.hostname.split('.')[-2:])
if main_domain in domain_filter_list:
    print('域名过滤',True)