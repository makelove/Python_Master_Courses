# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 09:33
# @Author  : play4fun
# @File    : str_is_number.py
# @Software: PyCharm

"""
str_is_number.py:
http://www.runoob.com/python3/python3-string-isnumeric.html

s.isdigit、isdecimal 和 s.isnumeric 区别：
isdigit()

True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字

False: 汉字数字

Error: 无

isdecimal()

True: Unicode数字，，全角数字（双字节）

False: 罗马数字，汉字数字

Error: byte数字（单字节）

isnumeric()

True: Unicode数字，全角数字（双字节），罗马数字，汉字数字

False: 无

Error: byte数字（单字节）

"""


num = "1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # True
num.isdecimal() # False
num.isnumeric() # True

num = "四" # 汉字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # True