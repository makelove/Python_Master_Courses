## pyinstaller

- 视频：https://www.bilibili.com/video/av21670971/

- PyInstaller可以用来打包python应用程序，打包完的程序就可以在没有安装Python解释器的机器上运行了。PyInstaller支持Python 2.7和Python 3.3+。可以在Windows、Mac OS X和Linux上使用，但是并不是跨平台的，而是说你要是希望打包成.exe文件，需要在Windows系统上运行PyInstaller进行打包工作；打包成mac app，需要在Mac OS上使用。

- 安装
    - pip isntall pyinstaller
    
- 使用
    - 命令行程序
        - pyinstaller helloworld.py
    - 窗口程序+命令行输出
        - pyinstaller happy_not.py
    - 只有窗口程序
        - pyinstaller -w happy_not.py
    
- 选项    
    - -D, --one-dir打包成一个文件夹，默认
    - -F, --one-file打包成一个exe文件
    - -p DIR, --paths DIR添加路径，一般用来添加程序所用到的包的所在位置
    - -c, --console, --nowindowed无视窗，程序后台运行
    - -w, --windowed, --noconsole 提供程序视窗，程序没有命令行输出，默认
    - -i <FILE.ico or FILE.exe,ID or FILE.icns>, --icon <FILE.ico or FILE.exe,ID or FILE.icns>添加icon图标