# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 23:17
# @Author  : play4fun
# @File    : tornado-crawler-demo2.py
# @Software: PyCharm

"""
tornado-crawler-demo2.py:
"""

# coding:utf8
import time
from datetime import timedelta

from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPResponse

try:
    from HTMLParser import HTMLParser
    from urlparse import urljoin, urldefrag
except ImportError:
    from html.parser import HTMLParser
    from urllib.parse import urljoin, urldefrag

from tornado import gen, ioloop, queues


class BaseSpider(object):
    def __init__(self, base_url, concurrency=10):
        self.q = queues.Queue()
        self.q2 = queues.Queue()
        self.start = time.time()
        self.fetching = set()
        self.fetched = set()
        self.base_url = base_url
        self.concurrency = concurrency
        self.i = 0

    def get_request(self, url, headers=None):
        response = None
        http_client = AsyncHTTPClient()
        try:
            # response = yield http_client.fetch(url, method='GET', headers=headers,request_timeout=5)

            # POST
            body = {'a': 4, 'b': 5}
            response: HTTPResponse = yield http_client.fetch(url, method='POST', body=str(body), headers=headers, request_timeout=5)
        except Exception as e:
            print('get_request error:{0}'.format(e))

        #请求
        response.request
        #请求头
        response.headers

        response_body = None
        if response and response.code == 200:
            # print('fetched {0}'.format(url))
            response_body = response.body if isinstance(response.body, str) \
                else response.body.decode()

        return response_body

    @gen.coroutine
    def get_links_from_url(self, url):
        try:
            # 获取该url对应的html页面
            html = yield self.get_request(url)

            # 获取该html里面所有的链接
            urls = [urljoin(url, self.remove_fragment(new_url))
                    for new_url in self.get_links(html)]
        except Exception as e:
            print('get_links_from_url error:{0}'.format(e))
            return []

        return urls

    # 将url '#' 后面的字符去掉，返回想要的链接
    def remove_fragment(self, url):
        pure_url, frag = urldefrag(url)
        return pure_url

    # 使用HTMLParser分析html，获取到里面的urls，也可以使用BeautifulSoup等.
    def get_links(self, html):
        class URLSeeker(HTMLParser):
            def __init__(self):
                HTMLParser.__init__(self)
                self.urls = []

            def handle_starttag(self, tag, attrs):
                href = dict(attrs).get('href')
                if href and tag == 'a':
                    self.urls.append(href)

        url_seeker = URLSeeker()
        url_seeker.feed(html)
        return url_seeker.urls

    @gen.coroutine
    def main(self):

        @gen.coroutine
        def fetch_url():
            current_url = yield self.q.get()
            print('current_url:{0}'.format(current_url))
            try:
                # 如果当前url正在获取中，return
                if current_url in self.fetching:
                    self.i += 1
                    return

                # print('fetching %s' % current_url)

                # 将当前url放入到fetching集合里面
                self.fetching.add(current_url)

                # 获取current_url页面里面所有的其他urls
                urls = yield self.get_links_from_url(current_url)

                # 将current_url放入到fetched集合里面
                self.fetched.add(current_url)

                # 将以base_url开头的url放入到队列q里面
                for new_url in urls:
                    # Only follow links beneath the base URL
                    if new_url.startswith(self.base_url):
                        yield self.q.put(new_url)
                        yield self.q2.put(new_url)

            finally:
                # 表明以前排队任务完成
                self.q.task_done()

        @gen.coroutine
        def worker():
            while True:
                yield fetch_url()

        # 将第一个url放入到q队列里面
        self.q.put(self.base_url)
        self.q2.put(self.base_url)

        # Start workers, then wait for the work queue to be empty.
        # 启动10个worker执行fetch_url()，因为是异步非阻塞的，这里是单线程异步爬虫。
        for _ in range(self.concurrency):
            worker()

        # 等到队列为空，再执行别的操作
        yield self.q.join(timeout=timedelta(seconds=300))

        # 重复获取抛出异常
        # assert self.fetching == self.fetched
        print(self.q2.qsize())
        print(
            'Done in %d seconds, fetched %s URLs.' % (time.time() - self.start, len(self.fetched)))

        print(self.i)

    def run(self):
        ioloop.IOLoop.current().run_sync(self.main)


class MySpider(BaseSpider):
    @gen.coroutine
    def get_request(self, url, headers=None):
        headers = {
            'User-Agent': 'mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        }
        return super(MySpider, self).get_request(url, headers=headers)


def run_spider():
    base_url = 'http://www.tornadoweb.org/en/stable/'
    concurrency = 10
    spider = MySpider(base_url, concurrency)
    spider.run()


if __name__ == '__main__':
    run_spider()
