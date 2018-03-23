## splash
- 视频：https://www.bilibili.com/video/av21142483/

- Splash是一个Javascript渲染服务。它是一个实现了HTTP API的轻量级浏览器，Splash是用Python实现的，同时使用Twisted和QT。Twisted（QT）用来让服务具有异步处理能力，以发挥webkit的并发能力。

- 官网
    - https://github.com/scrapinghub/splash

- 文档
    - https://splash.readthedocs.io/en/stable/
- 测试网站抓取
    - http://quotes.toscrape.com/js/
    
- 安装
    - 安装docker, 安装好后运行docker。
    - 拉取镜像
        - docker pull scrapinghub/splash
    - 运行splash
        - docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash
    - 安装scrapy-splash库
        - pip install scrapy-splash
        
- scrapy shell 例子
    - 不使用splash
        - scrapy shell http://quotes.toscrape.com/js/ 
    - 使用splash
        - scrapy shell 'http://localhost:8050/render.html?url=http://quotes.toscrape.com/js/' 
       
- You can run scrapy shell without arguments inside a configured Scrapy project, then create req = scrapy_splash.SplashRequest(url, ...) and call fetch(req).       