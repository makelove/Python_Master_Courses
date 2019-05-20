## 红米Note7 安装Charles-SSL证书

- 视频: https://www.bilibili.com/video/av53054984/

- 安装Charles
	- https://www.charlesproxy.com/download/
- 启动Charles
	- macOS系统代理
	- 浏览器打开http://chls.pro/ssl ,自动跳转到http://www.charlesproxy.com/getssl/
	- 自动下载证书
	- 改名,将pem格式改为crt格式
- 复制证书到MIUI系统
	- adb push charles-proxy-ssl-proxying-certificate.crt /storage/emulated/0/Download/
	- 安装,输入手机密码
		- 设置
		- 更多设置
		- 系统安全
		- 加密与凭据
		- 从SD卡安装
	- 启动-多点App
	- 获取-购物小票-数据
	- 使用requests抓取