# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 23:19
# @Author  : play4fun
# @File    : pyqt5_1.py
# @Software: PyCharm

"""
pyqt5_1.py:
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow

class MainWindow(QMainWindow):
# class MainWindow(QWebEnginePage):
    # noinspection PyUnresolvedReferences
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('My Browser')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/penguin.png'))
        # 设置窗口大小900*600
        self.resize(900, 600)
        self.show()


if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    window = MainWindow()
    # 显示窗口
    window.show()
    # 运行应用，并监听事件
    app.exec_()
