# -*- coding: utf-8 -*-
'''
凯撒加密法

只针对 字母 编码
数字不行
'''

import string


def encode(s, key='H'):
    rt = []
    for c in s.upper():  # 大写
        if c in string.ascii_uppercase:
            n = ord(c) + ord(key)
            if n > 90:
                n = n - 26
            c = chr(n)
        rt.append(c)
    return ''.join(rt)


def decode(s, key='H'):
    rt = []
    for c in s.upper():
        if c in string.ascii_uppercase:
            n = ord(c) - ord(key)
            if n < 65:
                n = n + 26
            c = chr(n)
        rt.append(c)
    return ''.join(rt)
