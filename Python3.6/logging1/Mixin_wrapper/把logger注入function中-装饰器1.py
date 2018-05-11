# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 11:35
# @Author  : play4fun
# @File    : 把logger注入function中-装饰器1.py
# @Software: PyCharm

"""
把logger注入function中-装饰器1.py:
"""

import logging, functools

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def debug(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function.__setattr__('logger', logger)
        result = function(*args, **kwargs)
        return result

    return wrapper


def debug2(function):
    function.__setattr__('logger', logger)

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


def wrap(func):  # 这个OK
    logger2 = logging.getLogger('wrap')
    func.__setattr__('logger', logger2)
    return func


# @debug2
@wrap
def foo(x, y, z):
    print(locals())
    log = foo.__get__('logger')
    # log2=foo.__getattribute__('logger')
    print('log:', logger, x, y, z, '\n')
    logger.error('Finished\n')  # TODO 报错！
    log.logger.error('Finished\n')  # TODO 报错！


# print(foo.__globals__)
# foo.__setattr__('logger',logger)#必须要设置，不然会报错



print(foo.__dict__)
x = foo(1, 2, 3)
# x=wrap(foo)(1,2,3)
