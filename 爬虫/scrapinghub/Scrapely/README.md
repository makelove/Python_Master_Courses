## Scrapely
- github主页：https://github.com/scrapy/scrapely

- Scrapely是一个可以从HTML网页中提取结构数据的库。给定一些网页例子和需要提取的数据，scrapely会对类似网站构造一个通用解析器。
    - Scractly提取基于实例基础学习算法[1]， 并且使用解析器树，从包装诱导的分层方法[2]中启发，将匹配项组合成复杂对象（它支持嵌套和重复对象）。

- 安装
    - pip install scrapely
    
    
- 首先导入scrapely模块
>>> from scrapely import Scraper
>>> s = Scraper()

- 加一些数据来训练你的scraper

>>> url1 = 'http://pypi.python.org/pypi/w3lib/1.1'
>>> data = {'name': 'w3lib 1.1', 'author': 'Scrapy project', 'description': 'Library of web-related functions'}
>>> s.train(url1, data)

- 训练结束后，这个scraper可以应用在所有类似网站
>>> url2 = 'http://pypi.python.org/pypi/Django/1.3'
>>> s.scrape(url2)
[{u'author': [u'Django Software Foundation <foundation at djangoproject com>'],
u'description': [u'A high-level Python Web framework that encourages rapid development and clean, pragmatic design.'],
u'name': [u'Django 1.3']}]    