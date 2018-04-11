# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 23:20
# @Author  : play4fun
# @File    : pyqt5_2.py
# @Software: PyCharm

"""
pyqt5_2.py:
https://my.oschina.net/wjgood/blog/887841
"""
import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel


# 1
class CallHandler(QObject):
    result = pyqtSignal(int)

    @pyqtSlot(str, result=int)
    def myHello(self, sss):
        print("js call py :" + sss)
        self.result.emit(8888)
        return 123


# 3
def _loadFinish(self, *args, **kwargs):
    view.page().runJavaScript("window.show()")
    print("load finish")




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 2
    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler()
    channel.registerObject('pyjs', handler)
    view.page().setWebChannel(channel)
    view.loadFinished.connect(_loadFinish)
    #
    htmlUrl = 'file:////Users/play/github/Python_Master_Courses/GUI图形界面/pyqt5/pyqt5-javascript-互相传值/1/js2.html'
    view.load(QUrl(htmlUrl))
    view.show()
    sys.exit(app.exec_())
