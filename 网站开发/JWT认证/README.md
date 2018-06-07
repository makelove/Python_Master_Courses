# JWT

- 参考
    - https://blog.csdn.net/cfy137000/article/details/79189252
    
```python

from django.core import signing
value = signing.dumps({"foo":"bar"})
print(value)

src = signing.loads(value)
print(src)

```    