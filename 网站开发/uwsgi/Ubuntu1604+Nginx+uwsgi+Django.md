## Ubuntu1604+Nginx+uwsgi+Django

- 安装 Ubuntu 16.04


- 安装python3.6
```bash
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6 python3.6-dev

```



- Python 虚拟环境
```bash
sudo apt install python3-pip
pip3 install virtualenv
pip3 install uwsgi
pip3 install django

django-admin startproject uwsgitest
sudo /home/play/.py3/bin/python manage.py runserver 0.0.0.0:80
http://192.168.187.131/
```
- uwsgi测试配置
```bash
#/home/play/TEST/uwsgitest/uwsgi1.ini
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/play/TEST/uwsgitest/
wsgi-file = uwsgitest/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191
master=true
py-autoreload = 1

# 指定IP端口   
#http=0.0.0.0:8002


#运行
uwsgi  uwsgi1.ini
http://192.168.187.131:8000/
```


- nginx配置
```bash
sudo apt install nginx-full

#sudo nano /etc/nginx/sites-available/default
#添加新的xxsite.conf
server {
        listen 80;
        listen [::]:80;

        server_name dg1.rrdaogou.com;


        location / {
                include uwsgi_params;
        uwsgi_pass   127.0.0.1:3031;
        }
}
        
# 重启Nginx
sudo service nginx restart
#运行
uwsgi  uwsgi1.ini
http://192.168.187.131
```
