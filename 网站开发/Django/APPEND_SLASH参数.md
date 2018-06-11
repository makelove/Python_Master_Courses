# APPEND_SLASH参数,自动在网址结尾加'/'

- 参考：
    - https://www.liurongxing.com/django-append_slash-true.html

- 方案
    - 在 settings.py中添加 APPEND_SLASH = False
    - 在urls.py 中配置 url模式，例如  /{0,}