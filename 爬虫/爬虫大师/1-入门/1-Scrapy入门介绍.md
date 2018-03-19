## Scrapy入门介绍

- 介绍
    - 官网https://scrapy.org/
    - Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架,用于抓取web站点并从页面中提取结构化的数据。
    - 命名：Scrap是碎片；残余物的意思，也可以说是搜刮
- Scrapy框架图
    - ![Scrapy框架图.jpg](Scrapy框架图.jpg)


- 中文文档
    - [Scrapy 1.3 文档](https://oner-wv.gitbooks.io/scrapy_zh/content/)
    - 1.0 文档 https://scrapy-chs.readthedocs.io/zh_CN/1.0/index.html
- 图书
    - [用Python写网络爬虫](https://item.jd.com/11963485.html)
    - [精通Python爬虫框架Scrapy](https://item.jd.com/12292223.html)
    - 国内作者：[精通Scrapy网络爬虫](https://item.jd.com/12207223.html)
    
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
    - 案例
        - scrapy startproject tutorial
```bash
scrapy startproject tutorial

New Scrapy project 'tutorial', using template directory '/Users/play/.py3/lib/python3.6/site-packages/scrapy/templates/project', created in:
    /Users/play/Study/Scrapy2018/tutorial

You can start your first spider with:
    cd tutorial
    scrapy genspider example example.com
```
        - cd tutorial
        - scrapy genspider quotes_spider quotes.toscrape.com
```bash
(.py3) pro:tutorial play$ scrapy genspider quotes_spider quotes.toscrape.com
Created spider 'quotes_spider' using template 'basic' in module:
  tutorial.spiders.quotes_spider
(.py3) pro:tutorial play$ tree
.
├── scrapy.cfg
└── tutorial
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   └── settings.cpython-36.pyc
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── __init__.py
        ├── __pycache__
        │   └── __init__.cpython-36.pyc
        └── quotes_spider.py
```            
- 复制python代码到  quotes_spider.py
```python
# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```
- 在工程的根目录执行爬虫
    - scrapy crawl quotes
```bash
2018-03-19 08:33:58 [scrapy.utils.log] INFO: Scrapy 1.4.0 started (bot: tutorial)
2018-03-19 08:33:58 [scrapy.utils.log] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}

2018-03-19 08:33:59 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2018-03-19 08:33:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2018-03-19 08:33:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)

2018-03-19 08:33:59 [quotes] DEBUG: Saved file quotes-2.html
2018-03-19 08:33:59 [quotes] DEBUG: Saved file quotes-1.html
2018-03-19 08:33:59 [scrapy.core.engine] INFO: Closing spider (finished)
2018-03-19 08:33:59 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 675,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 5976,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 3, 19, 0, 33, 59, 611662),
 'log_count/DEBUG': 6,
 'log_count/INFO': 7,
 'memusage/max': 50081792,
 'memusage/startup': 50081792,
 'response_received_count': 3,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2018, 3, 19, 0, 33, 58, 569183)}
2018-03-19 08:33:59 [scrapy.core.engine] INFO: Spider closed (finished)
```    
- 可以看到，爬虫把抓下来的HTML代码保存在html文件里面
```bash
(.py3) pro:tutorial play$ ls
.             ..            quotes-1.html quotes-2.html scrapy.cfg    tutorial
```

- 学习建议
    - 看完Scrapy中文文档
    - 购买一部Scrapy图书
    - 实战经验，多练习写代码，尝试爬取不同类型的网站，如电商，豆瓣，网贷，大众点评，微博，微信