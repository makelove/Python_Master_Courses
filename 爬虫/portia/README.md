## Portia 可视化的爬虫规则编写工具
- 官网
    - https://scrapinghub.com/portia
    - 源代码：https://github.com/scrapinghub/portia
    - 文档：https://portia.readthedocs.io/en/latest/getting-started.html
    
- 简介
    - Portia是scrapyhub开源的一款可视化的爬虫规则编写工具。它提供可视化的Web页面，你只需要通过点击标注页面上你需要抽取的数据，不需要任何编程知识即可完成规则的开发。
    
    
- 安装启动
    - 使用Docker
        - docker run -i -t -v /Users/play/Study/2018/portia:/app/data/projects:rw -p 9001:9001 scrapinghub/portia
        - 不要打开http://127.0.0.1:8000/
        - 入口是 http://127.0.0.1:9001/
```bash
docker run -i -t -v portia:/app/data/projects:rw -p 9001:9001 scrapinghub/portia

Unable to find image 'scrapinghub/portia:latest' locally
latest: Pulling from scrapinghub/portia
bae382666908: Pull complete
f1ddd5e846a8: Pull complete
90d12f864ab9: Pull complete
a57ea72e3176: Pull complete
783a14252520: Pull complete
33d1f4eba895: Pull complete
6accd3d6a8a4: Pull complete
cb3ce44e3a98: Pull complete
8ff8168c84ad: Pull complete
045fcce88b21: Pull complete
282b406db883: Pull complete
52c19f528131: Pull complete
3a917f6e6aa5: Pull complete
9fd0de65295a: Pull complete
0f4b5f29a395: Pull complete
Digest: sha256:79c2c8794e3411f5ae5585042aab6dabd439f1100422634470605ec62d2d9db1
Status: Downloaded newer image for scrapinghub/portia:latest
+ action=
+ shift
+ '[' -z '' ']'
+ _run
+ service nginx start
+ _set_env
+ path=/app/portia_server:/app/slyd:/app/slybot
+ export PYTHONPATH=/app/portia_server:/app/slyd:/app/slybot
+ PYTHONPATH=/app/portia_server:/app/slyd:/app/slybot
+ echo /app/portia_server:/app/slyd:/app/slybot
/app/portia_server:/app/slyd:/app/slybot
+ /app/portia_server/manage.py runserver
+ /app/slyd/bin/slyd -p 9002 -r /app/portiaui/dist
2018-03-21 06:17:55+0000 [-] Log opened.
2018-03-21 06:17:55.812093 [-] Splash version: 2.3.3
2018-03-21 06:17:55.814041 [-] WARNING: Lua scripting is not available because 'lupa' Python package is not installed
2018-03-21 06:17:55.814526 [-] Qt 5.5.1, PyQt 5.5.1, WebKit 538.1, sip 4.17, Twisted 17.9.0
2018-03-21 06:17:55.815100 [-] Python 2.7.6 (default, Nov 23 2017, 15:49:48) [GCC 4.8.4]
2018-03-21 06:17:55.816159 [-] Open files limit: 1048576
2018-03-21 06:17:55.816509 [-] Can't bump open files limit
2018-03-21 06:17:56.067923 [-] Xvfb is started: ['Xvfb', ':2091988890', '-screen', '0', '1024x768x24', '-nolisten', 'tcp']
2018-03-21 06:17:59.005542 [-] Site starting on 9002
2018-03-21 06:17:59.006193 [-] Starting factory <slyd.server.Site instance at 0x7f4391d330e0>
Performing system checks...

System check identified no issues (0 silenced).
March 21, 2018 - 06:18:00
Django version 1.10.5, using settings 'portia_server.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```        
        