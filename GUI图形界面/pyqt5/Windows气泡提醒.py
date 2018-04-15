# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 23:56
# @Author  : play4fun
# @File    : Windows气泡提醒.py
# @Software: PyCharm

"""
Windows气泡提醒.py:不行
在Windows ？？

"""

from PyQt5 import Qt
import sys
app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(app, Qt.QIcon('/Users/play/Downloads/jfdkke.jpg'))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')
sys.exit(app.exec_())