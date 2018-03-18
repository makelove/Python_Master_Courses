##1-virtualenv虚拟环境安装

- 视频：

- 什么是virtualenv？
    - python的虚拟环境，把你需要的工作环境与系统环境隔离，互不影响。
    - 因为python有很多版本，第三方包也有很多版本，有时候你需要特定版本，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。
    
- 安装
    - 安装python https://www.python.org/downloads/
    - 安装pip
        - https://pip.pypa.io/en/stable/installing/
            - >curl -o https://bootstrap.pypa.io/get-pip.py
            - >python get-pip.py
            - Ubuntu
                - sudo apt-get install python-pip python-dev build-essential 
                - sudo pip install --upgrade pip 
 
        - 配置镜像，避免安装过慢
```bash
vi ~/.pip/pip.conf

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```        

- 安装pip
     - pip install --upgrade virtualenv
     
-  virtualenv创建虚拟环境
    - python2.7
        - virtualenv .py2
    - python3.6
        - virtualenv -p python3 .py3 
    - 激活虚拟环境
         - source .py3/bin/activate
- 安装常用工具库
     - pip install ipython
     
- pip自动生成requirements.txt依赖关系清单
     - pip freeze > requirements.txt
