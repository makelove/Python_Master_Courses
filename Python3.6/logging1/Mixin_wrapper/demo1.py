# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 10:34
# @Author  : play4fun
# @File    : demo1.py
# @Software: PyCharm

"""
demo1.py:函数装饰器，写日志
"""

import logging,functools,sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)

def debug(function):
    @functools.wraps(function)
    def logged_function(*args,**kwargs):
        kwargs['logger']=logging
        logging.debug('%s(%r,%r)',function.__name__,args,kwargs,)
        result=function(*args,**kwargs)
        logging.debug('%s = %r)',function.__name__,result)
        return result
    return logged_function

@debug
def ackermann(m,n,**kwargs):
    #TODO 写日志
    log=kwargs.get('logger')
    log.debug('running ')
    if m==0:return n+1
    elif m>0 and n==0:return ackermann(m-1,1)
    elif m>0 and n>0:return ackermann(m-1,ackermann(m,n-1))

if __name__ == '__main__':
    ackermann(2,n=4)