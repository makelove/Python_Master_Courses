## 使用Item类封装数据

视频：

- 文档：https://oner-wv.gitbooks.io/scrapy_zh/content/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5/items.html
    - Item 对象是种简单的容器，保存了爬取到得数据。 其提供了 类似于词典(dictionary-like) 的API以及用于声明可用字段的简单语法。
    - Scrapy spider可以将解析结果用json返回，虽然方便，但项目大了，多了，不容易整理，容易出错。 

- 声明Item
```python
#tutorial/tutorial/items.py
import scrapy
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
```
- 使用
```python
import scrapy
from .. import items
from time import time

def parse_product(self,response):
    #parse 网页
    item=items.Product()
    item['name'] = '某个产品'
    item['price'] = 43.343
    item['stock'] = 32
    item['last_updated'] = str(int(time()))
    yield item
```