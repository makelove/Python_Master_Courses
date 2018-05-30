# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 09:09
# @Author  : play4fun
# @File    : 案例1-gevent.sleep.py
# @Software: PyCharm

"""
案例1-gevent.sleep.py:
"""

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(1)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])