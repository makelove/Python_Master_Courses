# -*- coding: utf-8 -*-
# @Time    : 2018/7/20 20:34
# @Author  : play4fun
# @File    : 报错-打印之前的变量.py
# @Software: PyCharm

"""
报错-打印之前的变量.py:
https://stackoverflow.com/questions/9059349/can-i-get-the-local-variables-of-a-python-function-from-which-an-exception-was-t
"""



def get_a_value():
    return 3 * 74


def myfunction():
    v1 = get_a_value()
    v2 = 'fdjlkg'
    raise Exception(locals())  # if you want all the local variables
    # raise Exception(v1)


try:
    myfunction()
except Exception as e:
    v1 = e.args[0]
    print(v1)

    # 所有变量
    print(e)

    #第3种方法
    import sys
    type, value, tb = sys.exc_info()
    while tb.tb_next:
        tb = tb.tb_next
    frame = tb.tb_frame
    print(frame.f_locals['v1'])
