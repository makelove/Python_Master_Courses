## 6-模拟登陆FormRequest

- 视频:https://www.bilibili.com/video/av21201800/

- 文档
    - https://doc.scrapy.org/en/latest/topics/request-response.html?highlight=FormRequest#formrequest-objects
    
- 测试网站：http://quotes.toscrape.com/login  
  - 用户名abc
  - 密码abc
  
- 爬虫
  - tutorial/tutorial/spiders/quote_login.py
  
- scrapy runspider quote_login.py -o quote-login.csv  