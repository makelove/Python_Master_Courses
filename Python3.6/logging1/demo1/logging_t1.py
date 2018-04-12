# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:30
# @Author  : play4fun
# @File    : logging_t1.py
# @Software: PyCharm

"""
logging_t1.py:
"""

# import logging
from time import sleep
#
# logging.basicConfig(level=logging.DEBUG,
#                     # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     # datefmt='%a, %d %b %Y %H:%M:%S',
#                     datefmt='%H:%M:%S',
#                     filename='myapp1.log',
#                     filemode='w')

from config import logging
from logging_t2 import testlog

from multiprocessing import Process

if __name__ == '__main__':
    p=Process(target=testlog,args=(10,))
    print('开始 Process')
    p.start()

    for x in range(20):
        print('for loop:',x)

        if x%3==0:
            logging.error('错误')
        if x%4==0:
            logging.fatal('致命错误')
        else:
            logging.debug('This is debug message')
            logging.info('This is info message')
            logging.warning('This is warning message')



        sleep(2)

    p.join()
    print('结束 Process')