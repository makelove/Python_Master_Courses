# -*- coding: utf-8 -*-
# @Time    : 2019-06-10 10:30
# @Author  : play4fun
# @File    : 选号算法.py
# @Software: PyCharm

"""
选号算法.py:
"""
import traceback
from datetime import datetime
import requests
from functools import reduce

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "authority": "reselleve.jd.com",
    "dnt": "1",
    "referer": "https://reselleve.jd.com/zslhyx.action?cardWid=4006241&bType=86&serviceOperatorId=4&provinceId=1&cityId=1&enc=14C11B5289C91A06&t=0.3828942636704814",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {#TODO 复制自己的cookies

}


def 只包含2个数字(cardNum: str):
    last4 = cardNum[-4:]
    s = set(last4)
    if len(s) == 2:
        print('只包含2个数字:\t', cardNum)

    pass


def 都是奇数或偶数(cardNum: str):
    last4 = cardNum[-4:]
    l奇数 = [int(num) % 2 == 1 for num in last4]
    l偶数 = [int(num) % 2 == 0 for num in last4]
    if reduce(lambda x, y: x & y, l奇数) == True:
        print('都是奇数:\t', cardNum)
    if reduce(lambda x, y: x & y, l偶数) == True:
        print('都是偶数:\t', cardNum)
    pass


def 数字大小顺序(cardNum: str):  # 从小到大 5678
    last4 = cardNum[-4:]
    l负一 = [int(x) - int(y) == -1 for x, y in zip(last4[:-1], last4[1:])]
    if reduce(lambda x, y: x & y, l负一) == True:
        print('数字从小到大排序:\t', cardNum)
    pass


def main():
    urlpre = 'https://reselleve.jd.com/queryPhoneNumList.action?cardWid=4006241&serviceOperatorId=4&bType=86&provinceId=19&cityId=1601&ownerInfoFlag=0&enc=A4138DF9EF270A6D&numberSegment=0&numberRule=0&keyWord=&t=0.5352053690691607&pageIndex='
    phoneList = []  # TODO 键值对	手机号:城市
    for index in range(10):
        url = urlpre + str(index)
        try:
            resp = requests.get(url, headers=headers, cookies=cookies)
            js = resp.json()
            l = [it['cardKey'] for it in js]
            phoneList += l
        except:
            print(traceback.format_exc())
    ps = set(phoneList)
    print('获取到', len(ps))
    input('暂停')
    for num in ps:
        只包含2个数字(num)
        都是奇数或偶数(num)
        数字大小顺序(num)
    pass


if __name__ == '__main__':
    print(datetime.now(), 'Start')
    try:
        main()
    except:
        print(traceback.format_exc())
    print(datetime.now(), 'Finished')
