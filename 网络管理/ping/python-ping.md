
- 参考
	- [ping的使用与实现原理剖析](https://zhuanlan.zhihu.com/p/36811342)
	- [如何使用Python ping（超级简单）](https://www.ictshore.com/python/python-ping-tutorial/)
- ping 域名
- ping t.cn -c 3
- ping 显示 路由
	- tracert t.cn
	- 

- 在macOS和Linux系统需要root权限
```
(.py3) pro:~ play$ which ipython
/Users/play/.py3/bin/ipython
(.py3) pro:~ play$ sudo /Users/play/.py3/bin/ipython
```

```
from pythonping import ping
response_list = ping('114.114.114.114', size=40, count=10)
response_list.rtt_avg_ms#毫秒

#判断网络是否连通
ip='192.168.0.2'
#ip='8.8.8.8'

rs = ping(ip, verbose=True,timeout=2)
1<=rs.rtt_avg<=2 #秒
```