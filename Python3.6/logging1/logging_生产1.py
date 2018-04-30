# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 16:16
# @Author  : play4fun
# @File    : logging_生产1.py
# @Software: PyCharm

"""
logging_生产1.py:
"""

#配置日志
import logging
from datetime import datetime
line_format='%(asctime)s %(funcName)s %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=line_format,
                    # datefmt="%H:%M:%S",
                    filename=datetime.now().strftime('tbk-%Y_%m_%d.log'),
                    filemode='a')
#
console = logging.StreamHandler()
# console.setLevel(logging.INFO)
formatter = logging.Formatter(line_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#
def log(*out):
    logging.debug(out)

def test():
    gl = [2, 34, 'g']
    log('test 你好', '我很好', 123, gl)
    logging.debug(('test 你好', '我很好', 123, gl))
print=log
print('你好','我很好',123,[2,34,'g'])
test()
print('end')