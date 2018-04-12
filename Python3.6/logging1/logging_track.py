# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 14:48
# @Author  : play4fun
# @File    : logging_track.py
# @Software: PyCharm

"""
logging_track.py:
"""

import sys

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Info level msg
logger.info('This is a standard message')
# Debug level msg
logger.debug('This is what you may want to see... sometimes...')
# Warning level msg
logger.info('This is what you are usually not happy to see')

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except Exception as e:
    #把错误堆栈打印出来
    # logger.error('Failed to read the file', exc_info=True)
    logger.debug('Failed to read the file', exc_info=True)
