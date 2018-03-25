## 8-Redis分布式抓取

- 人多力量大

- Redis以键值对形式存储数据，值的类型有
    - 字符串string
    - 哈希hash
    - 列表list
    - 集合set
    - 有序集合zset

- 安装
    - macOS
        - brew install redis
        - 启动 redis-server
    - Ubuntu Linux
        - sudo apt install redis-server
        - 启动 sudo service redis-server start
    - Redis 浏览器
        - sudo gem install redis-browser 
        - redis-browser --config ~/Desktop/redis-server-config.yml
    - 命令行 redis-cli    
    - 修改redis.conf以接受其他计算机访问
        - macOS：/usr/local/etc/redis.conf
        - Ubuntu：/etc/redis/redis.conf
            - bind 0.0.0.0
        - 测试
            - redis-cli -h 192.168.x.x
                - ping
                - pong
- Python
    - pip install redis
    - pip install scrapy-redis
        - 源代码https://github.com/rmax/scrapy-redis
- Scrapy 内调用
    - settings.py
    