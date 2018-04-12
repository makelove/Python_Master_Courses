# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:21
# @Author  : play4fun
# @File    : 简单的将日志打印到屏幕.py
# @Software: PyCharm

"""
简单的将日志打印到屏幕.py:
https://blog.csdn.net/yatere/article/details/6655445
"""

import logging
logging.basicConfig(level=logging.DEBUG)
'''
默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
日志级别大小关系为：
CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，
当然也可以自己定义日志级别。
'''

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')