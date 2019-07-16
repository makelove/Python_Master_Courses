# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 15:17
# @Author  : play4fun
# @File    : fib_setup.py
# @Software: PyCharm

"""
fib_setup.py:

python fib_setup.py build_ext --inplace

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# setup(
#     cmdclass={'build_ext': build_ext},
#     ext_modules=[Extension("myfib", ["fib.pyx"])]
# )
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules = cythonize("fib.pyx")
)
# ext_modules = cythonize("dot_cython.pyx"),
