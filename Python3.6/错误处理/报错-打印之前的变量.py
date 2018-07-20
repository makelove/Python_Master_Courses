# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 20:34
# @Author  : play4fun
# @File    : 报错-打印之前的变量.py
# @Software: PyCharm

"""
报错-打印之前的变量.py:
https://stackoverflow.com/questions/9059349/can-i-get-the-local-variables-of-a-python-function-from-which-an-exception-was-t
"""


import inspect

def get_a_value():
    return 3*74

def myfunction():
    v1 = get_a_value()
    raise Exception()

try:
    myfunction()
except:
    # can I access v1 from here?
    trace=inspect.trace()
    v1 = trace[-1][0].f_locals['v1']#在此断点
    print(v1)