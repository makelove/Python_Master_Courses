## Python从相对路径import
- 参考
    - https://blog.csdn.net/Yaokai_AssultMaster/article/details/77932522
    
- 将当前路径加入sys.path
    - 考虑到compontent和libs是处于同一级别的文件夹，我们可以直接在code.py中加入如下代码来把当前文件夹的母文件夹加入系统路径。    
```python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
```    
- 或者如下（这种情况对任何关系的文件夹都适用，只要我们在lib_path中给出到达该文件夹的绝对路径）：

```python
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
```
- 总结 ,我们实际上可以结合这两种方法：
```python
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( <path to the package> )
       from libs.some_lib import something
    else:
        from ..libs.some_lib import something
```