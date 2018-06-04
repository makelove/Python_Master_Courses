# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 14:23
# @Author  : play4fun
# @File    : exception.py
# @Software: PyCharm

"""
exception.py:
"""

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
