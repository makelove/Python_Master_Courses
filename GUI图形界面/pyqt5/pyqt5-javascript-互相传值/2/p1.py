# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 22:32
# @Author  : play4fun
# @File    : p1.py
# @Software: PyCharm

"""
p1.py:
http://www.cnblogs.com/yaoyu126/p/7524625.html
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl,pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

class CallHandler(QObject):
    @pyqtSlot(result=str)
    def myHello(self):
        print('call received')
        return 'hello, Python'

class CallHandler2(QObject):
    result = pyqtSignal(int)

    @pyqtSlot(str, result=int)
    def myHello(self, sss):
        print("js call py :" + sss)
        self.result.emit(8888)
        # 返回值需要使用回调函数去取到
        #https://stackoverflow.com/questions/43346199/returned-value-from-python-is-not-available-at-javascript?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
        return 123

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler2()
    channel.registerObject('pyjs', handler)
    view.page().setWebChannel(channel)

    url_string = "file:////Users/play/github/Python_Master_Courses/GUI图形界面/pyqt5/pyqt5-javascript-互相传值/2/test.html"
    view.load(QUrl(url_string))
    view.show()

    sys.exit(app.exec_())