# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:12
# @Author  : play4fun
# @File    : my_module2.py
# @Software: PyCharm

"""
my_module2.py:
"""
import logging
from autologging import logged, traced


@logged
@traced
class MyClass:
    def my_method(self, arg, keyword=None):
        self.__log.error("my message")
        return "%s and %s" % (arg, keyword)
