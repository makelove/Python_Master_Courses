# 爬虫-经验技巧

- scrapy crawl tutorial -o tutorial.json
    - 输出中文时，在json中显示是Unicode，而不是汉字
    - 解决
        - http://www.cnblogs.com/my8100/p/feed_export_encoding.html
        - 新建一个Pipeline，输出到json时，self.file.write(line.decode("unicode_escape"))
        - 最简单的方法
            - 修改 project的settings.py 
            - 添加 FEED_EXPORT_ENCODING = 'utf-8'