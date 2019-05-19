# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 15:13
# @Author  : play4fun
# @File    : fib_py.py
# @Software: PyCharm

"""
fib_py.py:
"""
import traceback
from datetime import datetime

import time


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


t = time.time()
rs = fib(40)
print('计算斐波那契数列', rs)  # 102334155
print(time.time() - t)  # 64.04913687705994
