# -*- coding: utf-8 -*-
# @Time    : 2019-11-15 12:43
# @File    : 抓取微信公众号文章列表1.py


"""
抓取微信公众号文章列表1.py:
"""

import requests, json
from pprint import pprint

def main():
    artL = []
    count = 0
    for i in range(10):  # 100条

        rs = requests.get(
            f"https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzUyMTY4MTk2OA==&f=json&offset=20&count={count}&is_ok=1&scene=126&uin=777&key=777&pass_ticket=ht6HnRgHEKNhxVp"
            f"%2BvvxUM5J7xfyTrMwCldHwN192lxsGh%2BZZPXLKNYXhJYOqqWG0&wxtoken=&appmsg_token=1035_G9nX10fQnLd%252FgHFQsxIbNkDEArrsO85BMhTX0A~~&x5=0&f=json",
            headers={
                "Host": "mp.weixin.qq.com",
                "accept": "*/*",
                "accept-language": "zh-cn",
                "referer": "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzUyMTY4MTk2OA==&scene=126&bizpsid=0&sharer_username=gh_b263da0eb84a&subscene=0&clicktime=1573792185&devicetype=iOS13.1.2&version=1700042d&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=94&pass_ticket=ht6HnRgHEKNhxVp%2BvvxUM5J7xfyTrMwCldHwN192lxsGh%2BZZPXLKNYXhJYOqqWG0&wx_header=1",
                "user-agent": "Mozilla/5.0 (iPod touch; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN",
                "x-requested-with": "XMLHttpRequest"
            },
            cookies={
                "devicetype": "iOS13.1.2",
                "lang": "zh_CN",
                "pass_ticket": "ht6HnRgHEKNhxVp+vvxUM5J7xfyTrMwCldHwN192lxsGh+ZZPXLKNYXhJYOqqWG0",
                "wap_sid2": "CMWh3vIFElwwVE1GNE13NG1LLWI1c0RJMGpJTXZsQmFDc3ZZV21OcWFUWDlqM1VLNzJDTU93SG9Ma1J2UnI3cWN5RlBFXzQ4VzhBN0pkR3h1NUVCcFBfaUFadXhtUXNFQUFBfjC607juBTgNQJVO",
                "wxuin": "1582796997"
            },
        )
        js = rs.json()
        # 列表
        l1 = json.loads(js['general_msg_list'])
        artL += l1['list']

        # 'next_offset': 30,
        count = js['next_offset']
        can_msg_continue = js['can_msg_continue']
        if can_msg_continue != 1:  # "can_msg_continue": 1,
            break

        pass
    print("len:", len(artL))
    print('-'*40)
    pprint(artL[-1])

    pass


if __name__ == '__main__':
    main()
