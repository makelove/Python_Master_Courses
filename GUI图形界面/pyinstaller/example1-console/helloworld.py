# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 11:24
# @Author  : play4fun
# @File    : helloworld.py
# @Software: PyCharm

"""
helloworld.py:
"""


def greeting(name: str):
    print('How are you ?' + name)


if __name__ == '__main__':
    print('Hello world !')
    name = 'Rose'
    greeting(name)
    # greeting(345)
