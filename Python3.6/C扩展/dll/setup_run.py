# -*- coding: utf-8 -*-
# @Time    : 2019-05-09 20:22
# @Author  : play4fun
# @File    : setup_run.py.py
# @Software: PyCharm

"""
setup_run.py.py:
macos编译
python setup_run.py build_ext --inplace

windows
python setup_run.py build_ext --inplace -c mingw32
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(name='str_add',
      ext_modules=cythonize('run.pyx', language_level=3))
