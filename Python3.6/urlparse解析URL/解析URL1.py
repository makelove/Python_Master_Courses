# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 10:04
# @Author  : play4fun
# @File    : 解析URL1.py
# @Software: PyCharm

"""
解析URL1.py:
"""
import urllib
from urllib.parse import urlparse

#淘宝客推广链接
url='https://detail.tmall.com/item.htm?id=561067099846&ali_trackid=2:mm_18989874_43894087_376356913:1525658813_216_155664132&pvid=10_182.48.115.66_547_1525658757001'
pas:urllib.parse.ParseResult=urlparse(url)
print(pas.scheme)#https
print(pas.netloc)#detail.tmall.com
print(pas.hostname)#detail.tmall.com
print(pas.query)#id=561067099846&ali_trackid=2:mm_18989874_43894087_376356913:1525658813_216_155664132&pvid=10_182.48.115.66_547_1525658757001

#解析query
from urllib.parse import parse_qs
query=parse_qs(pas.query)
print(query.keys())#dict_keys(['id', 'ali_trackid', 'pvid'])
print(query['id'])#['561067099846']
print(query['ali_trackid'])#['2:mm_18989874_43894087_376356913:1525658813_216_155664132']
