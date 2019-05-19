# -*- coding: utf-8 -*-
# @Time    : 2019-05-09 22:06
# @Author  : play4fun
# @File    : py_load_so.py
# @Software: PyCharm

"""
py_load_so.py:
"""
import traceback
from datetime import datetime

from ctypes import *


def main():
    test = cdll.LoadLibrary('./run.cpython-36m-darwin.so')
    add = test.add
    add.argtypes = [c_float, c_float]
    add.restype = c_float
    rs = add(1.3, 13.4)
    print('结果', rs)
    pass

def t2():
    pass

if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
