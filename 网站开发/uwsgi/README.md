## Django Nginx+uwsgi 安装配置

- 参考
    - 官方文档：http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
        - 中文 http://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/tutorials/Django_and_nginx.html
        - http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html#deploying-django
    - http://www.runoob.com/django/django-nginx-uwsgi.html
    - [通过Nginx部署Django（基于ubuntu)](https://www.cnblogs.com/fnng/p/5268633.html)
    
- 步骤
    - pip install uwsgi
    - uwsgi --version
    - 测试
        - uwsgi --http :8001 --wsgi-file test_uwsgi.py
        - http://127.0.0.1:8001/
    - 部署Flask 
        - http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html#deploying-flask