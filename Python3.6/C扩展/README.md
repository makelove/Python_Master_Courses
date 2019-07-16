- 视频: https://www.bilibili.com/video/av52977238/

- 官网
    - https://cython.org/
    - https://github.com/cython/cython
- 参考
    - 用cython 加速你的python代码 http://www.zhangdongshengtech.com/article-detials/212
    - python高性能扩展工具-cython教程1快速入门 https://www.jianshu.com/p/47c42ae044a0
    - language_level  是python的主版本号，如果python版本是2.x,目前的版本Cython需要人工指定language_level.
        - setup(name='str_add',ext_modules=cythonize('run.pyx', language_level=3))
    - Bash on Ubuntu on Windows
    -
- 用途
    - 在 Cython 中，类型标注对于提升速度是至关重要的。
    - 同时可以对你的代码加密

- 有多快
    - 常规Python函数，运行时间559 ns
    - Cython def函数，声明一个Python函数，既可以在模块内调用，也可以在模块外调用。模块内运行时间524.2 ns，模块外运行时间512 ns
    - Cython cpdef函数，声明一个C函数和一个Python wrapper，在模块内被当做C函数调用，在模块外被.py文件当做Python函数调用。模块内运行时间43.7 ns，模块外运行时间81.7 ns
    - Cython cdef函数，声明一个C函数，不可以在模块外被Python调用。模块内运行时间34.8 ns


- 文件后缀名
    - Linux cpython-36m-x86_64-linux-gnu.so
    - macOS cpython-36m-darwin.so
    - Windows cp36-win32.pyd
        - pyd 其实是dll文件

- 安装
    - Linux macOS
        - pip install Cython
    - Windows
        - pip install Cython
        - 安装 visual studio 2019
            - 2017不能下载了
        - 参考
            - Fix Python 3 on Windows error Microsoft Visual C++ 14.0 is required https://www.scivision.dev/python-windows-visual-c-14-required/
            - MinGW
                - https://blog.csdn.net/skh2015java/article/details/85075032
                - https://blog.csdn.net/qq_36731677/article/details/54608772


- 计算斐波那契数列