# -*- coding: utf-8 -*-
# @Time    : 2019-07-27 14:43
# @File    : ping_server_dingtalk.py
# @Software: PyCharm

"""
ping_server_dingtalk.py:

先安装
pip install pythonping
pip install dingtalkchatbot

运行，可能需要管理者权限
"""
from time import sleep
import sys, traceback
from pythonping import ping
from dingtalkchatbot.chatbot import DingtalkChatbot

# TODO  替换为你的机器人
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxxx'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)

# TODO 你的IP
server_list = [
    '192.168.1.100',
    '192.168.1.101',
    '192.168.1.102',
]


def main():
    print('开始运行')
    error_list = []

    for ip in server_list:
        rs = ping(ip, verbose=True,timeout=2)
        if 1 <= rs.rtt_avg <= 2:
            # TODO 发送到钉钉
            text = f'服务器{ip} ping 超时 {rs.rtt_avg}\n'
            xiaoding.send_text(text, is_at_all=True)
            error_list.append(ip)
            pass

    if len(error_list) == 0:
        text = f'服务器一切正常\n'
        xiaoding.send_text(text, is_at_all=True)
    print('结束')
    pass


if __name__ == '__main__':
    from time import sleep
    try:
        while True:#循环运行
            main()
            sleep(60 * 60)  # 1小时
    except:
        print(traceback.format_exc())
