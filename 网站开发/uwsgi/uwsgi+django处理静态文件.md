# uwsgi+django处理静态文件

- 参考
    - https://www.jianshu.com/p/38457576ce70
    - https://stackoverflow.com/questions/33168308/getting-404-for-all-static-files-during-wsgi-setup-with-django?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    
- 步骤
    - 在 setting.py 中新增配置 STATIC_ROOT 
```python
STATIC_ROOT = '/opt/nginx/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```         

- 执行 python manage.py collectstatic

- 修改 Nginx中关于Django项目的static配置
```bash
location /static {
        # alias /project/django/simpleblog/static;
        alias /opt/nginx/static;
    }
```

- 或者
```bash
You could also do it like so:

uwsgi --ini uwsgi.ini --http :8000 --static-map /static-/path/to/your/
or just add this to your .ini file:

static-map = /static=/path/to/staticfiles
```   