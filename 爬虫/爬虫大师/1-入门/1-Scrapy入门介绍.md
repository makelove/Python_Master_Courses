## Scrapy入门介绍

- 介绍
    - 官网https://scrapy.org/
    - Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。
- Scrapy框架图
    - ![Scrapy框架图.jpg](Scrapy框架图.jpg)


- 中文文档
    - [Scrapy 1.3 文档](https://oner-wv.gitbooks.io/scrapy_zh/content/)
    - 1.0 文档 https://scrapy-chs.readthedocs.io/zh_CN/1.0/index.html
    
- Scrapy 是用纯 Python 编写的，并且依赖于一些关键的 Python 包（其中包括）：
    - lxml ，一个高效的XML和HTML解析器
    - parsel ， 一个基于 lxml 的 HTML / XML 数据提取库
    - w3lib ，一个用于处理URL和网页编码的多用途助手
    - twisted， 一个异步的网络框架
    - cryptography 和 pyOpenSSL ，以处理各种网络级安全需求

- 安装
    - pip install scrapy
    
- 简单上手
    - 简单创建项目
        - scrapy startproject spider_name
        - 创建一个新的蜘蛛
            - scrapy genspider example example.com
        - 使用爬虫开始爬行scrapy crawl myspider

- 命令行工具
    - scrapy view http://www.example.com/some/page.html
    - scrapy shell http://www.example.com/some/page.html
    - scrapy parse http://www.example.com/ -c parse_item
    - scrapy runspider myspider.py