## pyqt5-HTML5调试-Chrome DevTools

- https://doc.qt.io/qt-5.10/qtwebengine-debugging.html
    - Qt WebEngine模块提供了Web开发工具，可以轻松检查和调试任何Web内容的布局和性能问题。
    - 开发人员工具可以使用基于Chromium或Qt WebEngine的浏览器（如Chrome浏览器）作为本地网页进行访问。



- 在cmd命令行后面 添加--remote-debugging-port=<port_number>
    - 例如 python3 pyqt5-html5-demo.py --remote-debugging-port=8123
    - 启动浏览器Chrome，打开http://localhost:<port_number>
    - 点击 URL，html
    - 进入  Chrome DevTools
    
- 可以设置环境变量QTWEBENGINE_REMOTE_DEBUGGING。它可以设置为只是一个工作方式类似于--remote-debugging-port主机地址或端口的端口。后者可用于控制将接口导出到哪个网络接口，以便您可以从远程设备访问开发人员工具。    

- --enable-logging --log-level=0启用控制台日志记录并将日志记录级别设置为0，这意味着严重级别info及更高级别的消息将记录在日志中。这是调试版本的默认值。其他可能的日志级别1用于警告，2错误和3致命错误。