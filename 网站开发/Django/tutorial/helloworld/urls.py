# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 21:32
# @Author  : play4fun
# @File    : urls.py
# @Software: PyCharm

"""
urls.py:
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
