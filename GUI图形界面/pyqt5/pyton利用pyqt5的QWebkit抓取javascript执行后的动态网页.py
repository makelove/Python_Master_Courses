# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 13:56
# @Author  : play4fun
# @File    : pyton利用pyqt5的QWebkit抓取javascript执行后的动态网页.py
# @Software: PyCharm

"""
pyton利用pyqt5的QWebkit抓取javascript执行后的动态网页.py:
https://blog.csdn.net/wolfwind521/article/details/42126549
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
# from lxml import etree
from lxml.etree import HTML

#use QtWebkit to get the final webpage
class WebRender(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.__loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def __loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

url=''
r = WebRender(url)
html = r.frame.toHtml()
page = HTML(html.encode('utf-8'))