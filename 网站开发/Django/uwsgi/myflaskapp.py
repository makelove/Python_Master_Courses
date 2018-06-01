# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 10:40
# @Author  : play4fun
# @File    : myflaskapp.py
# @Software: PyCharm

"""
myflaskapp.py:
运行：
uwsgi --socket 127.0.0.1:3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 -H /Users/play/github/Python_Master_Courses/.py3 --http :8002


"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')