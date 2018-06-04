# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 14:30
# @Author  : play4fun
# @File    : 最恰当的方式是继续往上抛，让顶层调用者去处理.py
# @Software: PyCharm

"""
最恰当的方式是继续往上抛，让顶层调用者去处理.py:
"""


def foo(s):
    n = int(s)
    return 10 / n


def bar(s):
    try:
        return foo(s) * 2
    except Exception as e:
        print('Error!')
        raise


def main():
    bar('0')


if __name__ == '__main__':
    main()
