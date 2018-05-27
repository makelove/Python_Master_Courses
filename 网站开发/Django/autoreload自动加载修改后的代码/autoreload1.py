# -*- coding: utf-8 -*-
# @Time    : 2018/5/27 14:26
# @Author  : play4fun
# @File    : autoreload1.py
# @Software: PyCharm

"""
autoreload1.py:
参考：
浅析 Django runserver 的 autoreload 功能
http://san-yun.iteye.com/blog/1612427
"""

from django.utils import autoreload

def test1():
    print('test1','不成功')

autoreload.main(test1())