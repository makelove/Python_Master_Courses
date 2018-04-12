# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:35
# @Author  : play4fun
# @File    : logging_t2.py
# @Software: PyCharm

"""
logging_t2.py:
"""
from config import logging
from time import sleep

def testlog(num):
    for x in range(num):


        if x%3==0:
            logging.error('错误')
        if x%4==0:
            logging.fatal('致命错误')
        else:
            logging.debug(str(x))

        sleep(3)
