# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 20:57
# @Author  : play4fun
# @File    : 午夜生成新log1.py
# @Software: PyCharm

"""
午夜生成新log1.py:
"""
from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler

logHandler = TimedRotatingFileHandler(filename="logs/logfile", when="midnight")
logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logHandler.setFormatter(logFormatter)

logger = logging.getLogger('MyLogger')
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

while True:
    for k in range(5):
        logger.info("Line %d" % k)
        sleep(3)