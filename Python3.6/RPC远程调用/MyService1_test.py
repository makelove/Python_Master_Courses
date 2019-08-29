# -*- coding: utf-8 -*-
# @Time    : 2019-08-13 19:08
# @File    : MyService1_test.py


"""
MyService1_test.py:
"""

import sys, traceback


def main(fp=None):
    pass


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        fp = sys.argv[1]
        try:
            main(fp)
        except:
            print(traceback.format_exc())
    else:
        print('python this.py filepath')
    