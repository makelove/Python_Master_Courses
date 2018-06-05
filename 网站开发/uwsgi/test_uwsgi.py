# -*- coding: utf-8 -*-
# @Time    : 2018/5/31 21:40
# @Author  : play4fun
# @File    : test_uwsgi.py
# @Software: PyCharm

"""
test_uwsgi.py:
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return "Hello World,uwsgi"#错的
    return [b"Hello World,uwsgi"]
