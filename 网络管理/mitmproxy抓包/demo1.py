# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 15:05
# @Author  : play4fun
# @File    : demo1.py
# @Software: PyCharm

"""
demo1.py:
参考
https://mitmproxy.org/#mitmdump
运行
mitmproxy -s mitmproxy1/demo1.py -p 8888

调试
import requests
proxies = { "http": "http://localhost:8888" }
rs=requests.get("http://example.com/", proxies=proxies)
print(rs.text)#重定向到mitmproxy.org

proxies = { "http": "http://localhost:8888" }
rs=requests.get("http://bing.com/brew", proxies=proxies)
print(rs.text)#"I'm a teapot"
"""

from mitmproxy import http


def request(flow: http.HTTPFlow):#拦截发出去的请求头/请求体等，也就是在数据尚未到达服务器的时候拦截
    # redirect to different host
    if flow.request.pretty_host == "example.com":
        flow.request.host = "mitmproxy.org"
    # answer from proxy
    elif flow.request.path.endswith("/brew"):
        flow.response = http.HTTPResponse.make(
            418, b"I'm a teapot",
        )
    return flow.request


def response(flow: http.HTTPFlow):#拦截返回头/返回体等，也就是数据从服务器返回的途中进行拦截。
    return flow.response