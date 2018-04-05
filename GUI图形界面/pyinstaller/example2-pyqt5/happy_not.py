# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 11:27
# @Author  : play4fun
# @File    : happy_not.py
# @Software: PyCharm

"""
happy_not.py:
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QDesktopWidget


def log(*msg):
    print(msg)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def btn_click(self):
        text = 'Not Happy😭' if self.label1.text() == 'Happy😀' else 'Happy😀'
        self.label1.setText(text)

        log('btn clicked:', self.label1.text())

    def initUI(self):
        happyB = QPushButton('Push me')
        happyB.clicked.connect(self.btn_click)

        self.label1 = QLabel('Happy😀')

        hbox = QVBoxLayout()
        hbox.addWidget(self.label1)
        hbox.addWidget(happyB)

        self.setLayout(hbox)

        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumWidth(250)
        self.setWindowTitle('Happy or Not')
        self.show()

        # 移动屏幕中间
        # centerPoint = QDesktopWidget().availableGeometry().center()
        # self.frameGeometry().moveCenter(centerPoint)
        # self.move(self.frameGeometry().topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
