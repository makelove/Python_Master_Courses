## 选择器（Selectors）-提取数据的机制

- 视频：https://www.bilibili.com/video/av20974346/
- 文档
    - [选择器（Selectors）](https://oner-wv.gitbooks.io/scrapy_zh/content/%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5/%E9%80%89%E6%8B%A9%E5%99%A8.html)

- 构造选择器
    - from scrapy.selector import Selector
    - from scrapy.http import HtmlResponse
-从文本构造：
    - body = '<html><body><span>good</span></body></html>'
    - Selector(text=body).xpath('//span/text()').extract()

- scrapy shell https://doc.scrapy.org/en/latest/_static/selectors-sample1.html
    - response.xpath('//title/text()')
    - response.css('title::text')
    - 提取第一个匹配的元素
        - response.xpath('//div[@id="images"]/a/text()').extract_first()
    - 嵌套选择器
        - response.xpath('//a[contains(@href, "image")]')
    - 通过正则表达式来提取数据
        - response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
        - response.xpath('//a[contains(@href, "image")]/text()').re_first(r'Name:\s*(.*)')
    - 注意 //node[1] 和 (//node)[1] 的区别
        - //node[1] 选择在其各自父节点下首先出现的所有 node。
        - (//node)[1] 选择文档中的所有 node，然后只获取其中的第一个节点。    
