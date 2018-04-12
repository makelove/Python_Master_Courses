# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:28
# @Author  : play4fun
# @File    : logger.conf例子3.py
# @Software: PyCharm

"""
logger.conf例子3.py:
"""

import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')