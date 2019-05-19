# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 15:27
# @Author  : play4fun
# @File    : test-f2.py
# @Software: PyCharm

"""
test-f2.py:
"""
import traceback
from datetime import datetime
from f2 import str_add

def main():

    rs = str_add('2312', '3545')
    print('结果:', rs)
    pass


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
