# -*- coding: utf-8 -*-
# @Time    : 2019-04-21 11:41
# @Author  : play4fun
# @File    : 比较速度.py
# @Software: PyCharm

"""
比较速度.py:
"""
import traceback
from datetime import datetime


def main():
    import time
    # 启动pyx编译器
    import pyximport
    pyximport.install()
    # Cython的素数算法实现
    import primesCy
    # Python的素数算法实现
    import primes

    print("Cython:")

    t1 = time.time()
    print(primesCy.primes(500))

    t2 = time.time()
    print("Cython time: %s" % (t2 - t1))

    print("")

    print("Python")

    t1 = time.time()
    print(primes.primes(500))

    t2 = time.time()
    print("Python time: %s" % (t2 - t1))


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
