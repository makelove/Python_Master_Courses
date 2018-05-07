# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 15:22
# @Author  : play4fun
# @File    : 午夜生成新log2.py
# @Software: PyCharm

"""
午夜生成新log2.py:
"""

from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler

line_format='%(asctime)s %(levelname)s %(funcName)s\t%(message)s'

logHandler = TimedRotatingFileHandler(filename="logs/tbk2.log", when="midnight")
# logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter(line_format)
logHandler.setFormatter(logFormatter)

logHandler.suffix = "%Y-%m-%d.log"

logger = logging.getLogger('MyLogger')
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter(line_format)
console.setFormatter(logFormatter)
logger.addHandler(console)


def fun1(st):
    logging.info(st)

def fun2(st):
    logger.info(st)

while True:
    for k in range(5):
        line = "Line %d" % k
        if k%2==0:
            fun1(line)
        else:
            fun2(line)
        # logger.info(line)
        sleep(3)