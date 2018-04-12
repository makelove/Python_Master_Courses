# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:34
# @Author  : play4fun
# @File    : config.py
# @Software: PyCharm

"""
config.py:
logmx 过滤器 log4j ：%d{HH:mm:ss} %-5p %m%n
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # format='%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d]  %(message)s',
                    format='%(asctime)s %(levelname)s  %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    datefmt='%H:%M:%S',
                    filename='myapp1.log',
                    # filemode='a')
                    filemode='w')
