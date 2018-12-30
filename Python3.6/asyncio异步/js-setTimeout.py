# -*- coding: utf-8 -*-
# @Time    : 2018-12-30 18:51
# @Author  : play4fun
# @File    : js-setTimeout.py
# @Software: PyCharm

"""
js-setTimeout.py:
参考
https://stackoverflow.com/questions/10154568/postpone-code-for-later-execution-in-python-like-settimeout-in-javascript
仿照JavaScript的setTimeout函数
"""
from datetime import datetime
import asyncio


def set_timeout(callback, seconds, *args):  # *args 是重点，传参
    async def schedule():
        await asyncio.sleep(seconds)
        print(datetime.now(), end=':\t\t')#检查时间
        callback(*args)

    asyncio.ensure_future(schedule())


def hello_world(name, age):
    print('welcome:', name, 'age:', age)


async def main():
    SleepTime=6
    print('Scheduling...')

    set_timeout(lambda: print('Now!'), 2)
    set_timeout(hello_world, 6, '张三', 18)  #秒数不能大于SleepTime

    print('Waiting...')

    await asyncio.sleep(SleepTime)#这个时间？
    print('END...')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
