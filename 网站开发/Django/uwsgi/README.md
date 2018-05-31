## Django Nginx+uwsgi 安装配置

- 参考
    - 官方文档：http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
    - http://www.runoob.com/django/django-nginx-uwsgi.html
    
- 步骤
    - pip install uwsgi
    - uwsgi --version
    - 测试
        - uwsgi --http :8001 --wsgi-file test_uwsgi.py
        - http://127.0.0.1:8001/