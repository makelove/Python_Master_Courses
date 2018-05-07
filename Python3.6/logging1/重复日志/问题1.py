# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 11:39
# @Author  : play4fun
# @File    : 问题1.py
# @Software: PyCharm

"""
问题1.py:
"""

import logging


def log(message):
    logger = logging.getLogger('testlog')

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    streamhandler.setFormatter(formatter)

    logger.addHandler(streamhandler)
    logger.error(message)

if __name__ == '__main__':
    log('hi')
    log('hi too')
    log('hi three')