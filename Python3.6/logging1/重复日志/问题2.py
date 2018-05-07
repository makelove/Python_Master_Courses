# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 11:39
# @Author  : play4fun
# @File    : 问题1.py
# @Software: PyCharm

"""
问题1.py:
"""

import logging
from logging.handlers import TimedRotatingFileHandler


def logger():
    logger = logging.getLogger('testlog')

    logHandler = TimedRotatingFileHandler(filename="logfile", when="midnight")
    logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    logHandler.setFormatter(logFormatter)



    if not logger.handlers:
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        streamhandler.setFormatter(formatter)

        logger.addHandler(streamhandler)
        logger.addHandler(logHandler)


    # logger.error(message)
    return logger

if __name__ == '__main__':
    log=logger()
    log.error('hi')
    log.error('hi too')
    log.error('hi three')

    log = logger()
    log.error('hi')
    log.error('hi too')
    log.error('hi three')

    log = logger()
    log.error('hi')
    log.error('hi too')
    log.error('hi three')

    log = logger()
    log.error('hi')
    log.error('hi too')
    log.error('hi three')