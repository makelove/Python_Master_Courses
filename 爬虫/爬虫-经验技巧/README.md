# 爬虫-经验技巧

- scrapy crawl tutorial -o tutorial.json
    - 输出中文时，在json中显示是Unicode，而不是汉字
    - 解决
        - http://www.cnblogs.com/my8100/p/feed_export_encoding.html
        - 新建一个Pipeline，输出到json时，self.file.write(line.decode("unicode_escape"))
        - 最简单的方法
            - 修改 project的settings.py 
            - 添加 FEED_EXPORT_ENCODING = 'utf-8'
            
- 在pycharm里调试，断点，单步调试
    - 在工程根目录添加main.py
```python
from scrapy import cmdline
cmdline.execute("scrapy crawl tutorial".split())
```    


- 使用Firebug需要安装Firefox 39.0b7.dmg
    - [新版本的Firefox浏览器不支持firebug JS调试的问题](https://blog.csdn.net/m0_37871052/article/details/74579034)
        - https://archive.mozilla.org/pub/firefox/releases/39.0b2/win64/zh-CN/