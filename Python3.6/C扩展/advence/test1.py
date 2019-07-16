# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 11:55
# @Author  : play4fun
# @File    : test1.py
# @Software: PyCharm

"""
test1.py:
"""
import traceback
from datetime import datetime


def main():
    import advence_cy
    advence_cy
    pass


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')