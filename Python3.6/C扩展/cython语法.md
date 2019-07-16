- 视频: https://www.bilibili.com/video/av53266371/

- 参考
    - python高性能扩展工具-cython教程2基础 https://www.jianshu.com/p/b6c7f54e8692

    - Cython基本用法 https://www.jianshu.com/p/5d078a4de156

    - Optimizing with Cython Introduction - Cython Tutorial https://pythonprogramming.net/introduction-and-basics-cython-tutorial/



cython -a dfjk.pyx
生成html文件,用浏览器打开

1. Cython是什么?

Cython是一个编程语言，它通过类似Python的语法来编写C扩展并可以被Python调用.既具备了Python快速开发的特点，又可以让代码运行起来像C一样快，同时还可以方便地调用C library。

2. 如何安装Cython?

跟大多数的Python库不同，
Cython需要一个C编译器，在不同的平台上配置方法也不一样。

准确说Cython是单独的一门语言，专门用来写在Python里面import用的扩展库。实际上Cython的语法基本上跟Python一致，而Cython有专门的&ldquo;编译器&rdquo;先将 Cython代码转变成C（自动加入了一大堆的C-Python API），然后使用C编译器编译出最终的Python可调用的模块。

https://www.jianshu.com/p/5d078a4de156
Cython 程序需要先编译之后才能被 Python 调用，流程是：

1.Cython 编译器把 Cython 代码编译成调用了 Python 源码的 C/C++ 代码
2.把生成的代码编译成动态链接库
3.Python 解释器载入动态链接库

在 Cython 中，类型标注对于提升速度是至关重要的。

Cython 中类型声明非常重要，但是我们不加类型标注它依然是一个合法的 Cython 程序，所以自然而然地，我们会担心漏加类型声明。不过好在 Cython 提供了一个很好的工具，可以方便地检查 Cython 程序中哪里可能可以进一步优化。
cython -a dot_cython.pyx
如果当前 Cython 程序用到了 C++，那么还得加上 --cplus 参数。在成功运行完 cython -a 之后，会产生同名的 .html 文件。

要点
1.cdef 函数不能被python直接调用,所以要写def函数调用cdef 函数
2.e

