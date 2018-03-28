# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 16:27
# @Author  : play4fun
# @File    : main.py
# @Software: PyCharm

"""
main.py:
"""

from scrapy import cmdline
# cmdline.execute("scrapy crawl music".split())
cmdline.execute("scrapy crawl music_phone".split())