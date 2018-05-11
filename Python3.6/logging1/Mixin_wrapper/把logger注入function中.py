# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 11:34
# @Author  : play4fun
# @File    : 把logger注入function中.py
# @Software: PyCharm

"""
把logger注入function中.py:
"""

import logging
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def foo(x, y, z):
    log=foo.__get__('logger')
    print('locals',locals(),'\n')
    log.logger.error('Finished\n')

# print(foo.__globals__)
foo.__setattr__('logger',logger)#必须要设置，不然会报错


print('__dict__',foo.__dict__)
x=foo(1,2,3)