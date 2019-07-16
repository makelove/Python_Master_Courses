# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 11:41
# @Author  : play4fun
# @File    : setup.py
# @Software: PyCharm

"""
setup.py:

python setup.py build_ext --inplace

安装到本地
python setup.py install
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name='advence_cy',
    version='19.05.13.20',  # 按日期
    ext_modules=cythonize(Extension(
        'advence_cy',
        sources=['a.pyx', ],  # 'b.pyx' #TODO 不能2个以上?
        language='c',

    ), language_level=3))
