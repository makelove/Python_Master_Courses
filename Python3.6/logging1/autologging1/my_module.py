# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 15:02
# @Author  : play4fun
# @File    : my_module.py
# @Software: PyCharm

"""
my_module.py: 没什么用
"""

from autologging import logged, traced
import sys
import logging
logging.basicConfig(
    level=logging.DEBUG, stream=sys.stdout,
     format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")

@logged
@traced
class MyClass:
    def my_method(self, arg, keyword=None):
        print('start')
        self.__log.info("my message")
        return "%s and %s" % (arg, keyword)

MyClass().my_method('hello','world')

# if __name__ == '__main__':
#     myc=MyClass()
#     rt=myc.my_method('hello','world')
#     print(rt)