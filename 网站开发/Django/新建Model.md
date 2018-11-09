

- 外键
    - 新建对象时，外键需要传递【对象】,不是对象的id
        - pu = PID_User(pid=pid_object, user=user_object)
        - pu.save()

- shell
    - python manage.py shell
```python
from main.models import User
us=User.objects.all()
```    