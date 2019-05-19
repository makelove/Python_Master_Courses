# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 15:21
# @Author  : play4fun
# @File    : cython_fib.py
# @Software: PyCharm

"""
cython_fib.py:
测试
"""
import traceback
from datetime import datetime

import myfib
import time

t = time.time()
# rs=myfib.fib(40)
rs=myfib.fib_c(40) #秒 0.6429920196533203
print('计算斐波那契数列', rs)
print(time.time() - t)#9.496641874313354

#修改fib.pyx : int n 后
#9.321077823638916