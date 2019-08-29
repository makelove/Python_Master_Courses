# -*- coding: utf-8 -*-
# @Time    : 2019-08-13 19:07
# @File    : MyService1.py


"""
MyService1.py:
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
    