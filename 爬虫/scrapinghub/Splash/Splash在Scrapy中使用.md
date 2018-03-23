## Splash在Scrapy中使用
- 参考
    - http://www.cnblogs.com/zhonghuasong/p/5976003.html

配置splash服务（以下操作全部在settings.py）：

1）添加splash服务器地址：

SPLASH_URL = 'http://localhost:8050'  
2）将splash middleware添加到DOWNLOADER_MIDDLEWARE中：

DOWNLOADER_MIDDLEWARES = {
'scrapy_splash.SplashCookiesMiddleware': 723,
'scrapy_splash.SplashMiddleware': 725,
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
3)Enable SplashDeduplicateArgsMiddleware:

SPIDER_MIDDLEWARES = {
'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
4)Set a custom DUPEFILTER_CLASS:

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
5)a custom cache storage backend:

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'