# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 23:12
# @Author  : play4fun
# @File    : tornado-async-spider.py
# @Software: PyCharm

"""
tornado-async-spider.py:
"""

# coding=utf-8
"""
tornado异步爬虫示例

"""
import time
from datetime import timedelta
from bs4 import BeautifulSoup
from tornado.httpclient import AsyncHTTPClient
from tornado import ioloop, gen, queues

_q = queues.Queue()


@gen.coroutine
def fetch(url):
    print('fetcing', url)
    response = yield AsyncHTTPClient().fetch(url, raise_error=False)

    #POST

    raise gen.Return(response)


@gen.coroutine
def run():
    try:
        url = yield _q.get()
        res = yield fetch(url)
        html = res.body
        soup = BeautifulSoup(html, "html.parser")
        print(str(soup.find('title')))
    finally:
        _q.task_done()


@gen.coroutine
def worker():
    while not _q.empty():
        yield run()


@gen.coroutine
def main():
    for i in range(73000, 73100):  # 放100个链接进去
        url = "http://www.jb51.net/article/%d.htm" % i
        yield _q.put(url)

    for _ in range(100):  # 模拟100个线程
        worker()

    yield _q.join(timeout=timedelta(seconds=30))


if __name__ == '__main__':
    s = time.time()
    ioloop.IOLoop.current().run_sync(main)
    print('use time:', time.time() - s)
