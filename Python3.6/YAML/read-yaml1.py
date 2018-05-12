# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 17:53
# @Author  : play4fun
# @File    : read-yaml1.py
# @Software: PyCharm

"""
read-yaml1.py:

pip install pyyaml

"""

# 加载yaml
import yaml

# 读取文件
f = open('test1.yaml','rb')

# 导入
x = yaml.load(f)

# print(x)
# print(type(x))
urls = x['url']

for it in urls:
    for k, v in it.items():
        print(k)
        for url in v:
            print(url)
