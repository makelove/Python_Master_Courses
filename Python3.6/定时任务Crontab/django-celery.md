I use celery to create my periodical tasks. First you need to install it as follows:
```bash
pip install django-celery
```
Don't forget to register django-celery in your settings and then you could do something like this:
```python

from celery import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
@periodic_task(run_every=crontab(minute="0", hour="23"))
def do_every_midnight():
 #your code
```
