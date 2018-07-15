# -*- coding: utf-8 -*-
# @Time    : 2018/7/15 14:52
# @Author  : play4fun
# @File    : QwebEngineView_cookies操作.py
# @Software: PyCharm

"""
QwebEngineView_cookies操作.py:
参考
https://zhuanlan.zhihu.com/p/32390678
"""

import sys
from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings, QWebEnginePage
from PyQt5.QtWidgets import QApplication



class sample(QWebEngineView):
    DomainCookies = {}

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('cookie操作演示')
        url = 'https://zhuanlan.zhihu.com/p/32390678'
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self.onCookieAdd)
        self.loadFinished.connect(self.onLoadFinished)
        self.show()
        self.load(QUrl(url))

    def onLoadFinished(self):
        for name in self.DomainCookies:
            print(name, self.DomainCookies[name])

    def onCookieAdd(self, cookie):
        if 'zhihu.com' in cookie.domain():
            name = cookie.name().data().decode('utf-8')
            value = cookie.value().data().decode('utf-8')
            if name not in self.DomainCookies:
                self.DomainCookies.update({name: value})
                print('onCookieAdd:',name,value)

'''#输出
onCookieAdd: tgw_l7_route bc9380c810e0cf40598c1a7b1459f027
onCookieAdd: _xsrf 67500afe-cbf6-484a-b8ae-712186647a95
onCookieAdd: d_c0 "ACDntOpB5w2PTn2wy6F4GG5Kn2hDt0Xpwtk=|1531637726"
onCookieAdd: q_c1 9df2575020e7487fb0d49eddd1c2b091|1531637726000|1531637726000
tgw_l7_route bc9380c810e0cf40598c1a7b1459f027
_xsrf 67500afe-cbf6-484a-b8ae-712186647a95
d_c0 "ACDntOpB5w2PTn2wy6F4GG5Kn2hDt0Xpwtk=|1531637726"
q_c1 9df2575020e7487fb0d49eddd1c2b091|1531637726000|1531637726000
onCookieAdd: _zap 53e2c0d4-9092-4afd-9396-6b5349e5eeb6

'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = sample()
    sys.exit(app.exec_())
