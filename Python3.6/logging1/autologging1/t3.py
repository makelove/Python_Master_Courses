# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:16
# @Author  : play4fun
# @File    : t3.py
# @Software: PyCharm

"""
t3.py:
"""


import sys
from autologging import TRACE, traced, logged

import logging
logging.basicConfig(
    level=TRACE, stream=sys.stdout,
    format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")

@logged
@traced
def gen_func(x, y):
    yield x + y
    yield x + y + 1
    return 'return'

print('-------')
for a in gen_func(7, 9):
    print(a)
    pass
'''
TRACE:__main__:gen_func:CALL *(7, 9) **{}
TRACE:__main__:gen_func:RETURN <generator object gen_func at 0x1091ed360>
16
17

'''