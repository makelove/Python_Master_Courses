# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 11:56
# @Author  : play4fun
# @File    : Timer1.py
# @Software: PyCharm

"""
Timer1.py:
https://stackoverflow.com/questions/573618/django-set-up-a-scheduled-job

"""

from threading import Timer
# Timer?
from datetime import datetime


def sync():
    print(datetime.now(), 'Running...')

    sync_timer = Timer(4, sync, ())#4秒运行一次
    sync_timer.start()


sync()
# 会一直运行，不会停止
