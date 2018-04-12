# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:29
# @Author  : play4fun
# @File    : logger.conf例4.py
# @Software: PyCharm

"""
logger.conf例4.py:
"""

import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example02")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')