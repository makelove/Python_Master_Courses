## LinkExtractor
- 视频：

- 文档：https://docs.scrapy.org/en/latest/topics/link-extractors.html

- LinkExtractor介绍
    - 专门用于提取链接的类，在提取大量链接或提取比较复杂时，用LinkExtractor更方便
    
- 使用
    - scrapy shell https://www.hao123.com/
    - from scrapy.linkextractors import LinkExtractor
    - le=LinkExtractor()#默认提取所有链接
    - links=le.extract_links(response)
```python
pattern='^http://www.hao123'
le=LinkExtractor(allow=pattern)
le.extract_links(response)

le=LinkExtractor(deny=pattern)
le.extract_links(response)


le=LinkExtractor(tags='script',attrs='src')
le.extract_links(response)
```    
