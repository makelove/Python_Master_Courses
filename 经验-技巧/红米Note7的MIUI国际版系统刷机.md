## 小米手机-红米Note7的MIUI国际版系统刷机

- 视频: https://www.bilibili.com/video/av51815115/

1. 购买-广发-发现精彩App,使用信用卡分3期购买

2. 解锁,等上15天
3. 下载解锁程序,解锁
    - https://www.miui.com/unlock/index.html
    - 同时按音量-键和电源键,进入FlashBoot模式
    - 解锁会重置手机,一定要保存相片和其他资料

4. 下载FlashBoot刷机软件:
    - http://en.miui.com/a-234.html
    - MIUI ROM Flashing Tool http://api.en.miui.com/url/MiFlashTool
5. 下载MIUI国际版系统
    - http://en.miui.com/a-234.html
    - ★ Redmi Note 7 Latest Global Stable Version Fastboot File Download
6. 同时按音量-键和电源键,进入FlashBoot模式
    - 刷机成功,自动重启

7. 初始化配置,需要翻墙连接Google服务器
8. 在自己的电脑上安装代理软件,共享给手机
    - 安装Shadowsocks,配置国外服务器,实现本机能翻墙
        - 参考:Shadowsocks + Privoxy 搭建 http 代理服务 https://my.oschina.net/icebergxty/blog/1860519
    - 安装privoxy
        - 参考:MacOS上的ShadowSocks代理共享给其他设备 https://blog.eson.site/archives/892
        - brew install privoxy
        - 修改配置/usr/local/etc/privoxy/config
            - forward-socks5t
            - listen-address
        - 启动代理
            - /usr/local/Cellar/privoxy/3.0.28/sbin/privoxy /usr/local/etc/privoxy/config
9. 手机连接WIFI,设置代理
    - 主机:电脑IP
    - 端口:listen-address所写的:8118
10. 连上Google,继续配置

11. 进入系统,使用Google Play安装App

## 刷机成功!