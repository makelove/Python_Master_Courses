# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 23:19
# @Author  : play4fun
# @File    : pyqt5_1.py
# @Software: PyCharm

"""
pyqt5_1.py:
"""
import sys
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal,QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWebEngineWidgets import  QWebEngineView,QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

# 1
class CallHandler2(QObject):
    result = pyqtSignal(int)

    @pyqtSlot(str, result=int)
    def myHello(self, sss):
        print("js call py :" + sss)
        self.result.emit(8888)
        return 123

class CallHandler3(QObject):
    @pyqtSlot()
    def test(self):
        print('call received')

class CallHandler(QObject):
    @pyqtSlot(result=str)
    def myHello(self):
        print('call received')
        return 'hello, Python'

# class MainWindow(QMainWindow):
class MainWindow(QWebEnginePage):
    # noinspection PyUnresolvedReferences
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        # self.setWindowTitle('My Browser')
        # 设置窗口图标
        # self.setWindowIcon(QIcon('icons/penguin.png'))
        # 设置窗口大小900*600
        # self.resize(900, 600)
        # self.show()



        # 2
        self.view = QWebEngineView()
        channel = QWebChannel()
        handler = CallHandler()
        channel.registerObject('handler', handler)
        self.view.page().setWebChannel(channel)
        self.view.loadFinished.connect(self._loadFinish)


        # 添加浏览器到窗口中
        # self.setCentralWidget(self.view)

        #
        htmlUrl = 'file:////Users/play/github/Python_Master_Courses/GUI图形界面/pyqt5/pyqt5-javascript-互相传值/js1.html'
        self.view.load(QUrl(htmlUrl))
        self.view.show()

    # 3
    def _loadFinish(self, *args, **kwargs):
        # self.view.page().runJavaScript("window.show()")
        self.view.page().runJavaScript("call_python()")
        print("qt load finish view.loadFinished.connect(self._loadFinish)")





if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    window = MainWindow()
    # 显示窗口
    # window.show()
    # 运行应用，并监听事件
    app.exec_()
