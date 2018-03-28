# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 17:36
# @Author  : play4fun
# @File    : 群发消息-文本-1.py
# @Software: PyCharm

"""
群发消息-文本-1.py:
"""
import requests, json
from urllib.parse import urlencode, unquote


# 使用测试号


def getWxAccessToken():
    APPID = 'wxca10980ebf50a876'
    APPSECRET = '68e7da7078ef97a9a260fa7c149a80af'

    #
    # APPID = 'wx1c19f3f693c86c6d'
    # APPSECRET = 'e6cfa83986d8995bd20c73567babcf3d'
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + APPID + '&secret=' + APPSECRET
    print(url)
    rs = requests.get(url)
    js = rs.json()
    print(js)
    '''
    {'access_token': '8__DozA3nc8TTPFfcQKslNqVcH18oFTkC6iYjenjEjX2CUJOGHAtY7OzMYB9raYHhh7ijUt10AhuWoQcllogV2Ri6p2zkFtiamuF6t35GH3AU742QtxDitc6Z4-i_47DhOq9_CKmgKYwmaklCkLKMaAHAGFH', 'expires_in': 7200}
    '''
    return js


def sendMsgAll():  # 群发接口
    # 1.获取全局access_token
    # access_token = getWxAccessToken()
    access_token = '8_Ex_q6HZoTy-GnMdTvyFuqfvhHErfAYlMVriOj9nr7FdAYh8xXZ_6zFoe2hBqAMzCTgtSMsIS1fgWZCb9g2FjukQQop-JA_j6pRHoKjBggT7Wi7IPpYnC_ai9rzjftDhm21kk4jqkTS79m17QTIOcAHAYNT'
    # url = 'https://api.weixin.qq.com/cgi-bin/message/mass/preview?access_token=' + access_token
    url = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token=' + access_token
    # 2.组装群发接口数据array
    c = "Test测试群发接口,OK"
    c = "先用urlencode是因为中文在数组转json时会被编码为unicode，微信接口无法识别，所以得在json_encode前先来个编码，等转换后再用urldecode转回来，这样传输给接口的就是正常的中文了"
    c = '''清明节将至，又到了菊花销售旺季。近日，记者走访阳春市潭水镇的花卉园地看到，花农正忙着采收菊花。据悉，目前菊花收购价格为1.2元每支，比去年同期涨了三成左右。
   记者在潭水镇旗鼓村鱼田自然村附近的一块花田看到，菊花开满枝头，有黄的、白的，还有紫色的，各自成片，煞是好看。几名花农正穿梭在菊花地里，忙着采收白菊。花农谢先生一边采收菊花，一边告诉记者，目前正是菊花销售旺季，他和几名工人每天要采收1万多支菊花，从早上8点到下午5点，晚上打好包装就可以上市销售了。谢先生说，菊花的生长周期一般是120天左右，他今年共种植了10亩菊花，现在已经采收得差不多了，今年的产量和行情都不错，亩产大约5万支，一亩菊花收入在6万元左右。
  今年菊花行情特别好，价格每天都在涨，预计到清明节前几天要卖到1.5元每支。”26日，阳春市花卉协会会长谢绍辉告诉记者，连日来正是菊花采收上市的旺季，花农们抓住时机，大量采收菊花。
   据介绍，近年来潭水镇合理调整生产布局，优化产业品种结构，把花卉生产作为引领农民增收致富的路子，实行分类指导、连片种植，并列入现代农业园区建设，建立以旗鼓、新凤、翔南等村为主的花卉生产基地。目前，潭水镇菊花种植面积约有2000亩，以白菊花、黄菊花、紫菊花等品种为主，畅销珠三角及省内外。
    '''
    array = {
        "touser": 'oFDDSw8piGrzW-Ul9E9EA1M1aQ3c',  # 微信用户的openID,#测试账号
        # "text": {"content": json.dumps(c,ensure_ascii=False)},  # 文本内容
        "text": {"content": c},  # 文本内容
        "msgtype": "text"  # 消息类型
    }
    # 单图文
    array2 = {
        "touser": 'oFDDSw8piGrzW-Ul9E9EA1M1aQ3c',
        "image": {
            "media_id": "123dsdajkasd231jhksad"
        },
        "msgtype": "image"
    }
    array = {
        "filter": {
            "is_to_all": True,
            # "tag_id":2
        },
        "text": {
            "content": c
        },
        "msgtype": "text"
    }

    body = json.dumps(array, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    data = body.encode('utf-8')

    # 3.将array转成json
    # 4.调用curl
    # headers={'content-type': 'application/json;charset=utf-8'}
    # headers = {'Content-type': 'application/json;charset=utf-8'}
    headers = {
        'Content-Type': 'application/json',
        'content-encoding': "utf-8"
    }

    # rs=requests.post(url,data=data,headers=headers)
    rs = requests.post(url, data=data)
    # rs = requests.post(url, data=json.dumps(array, False))
    # rs=requests.post(url,data=array,headers=headers)
    print(rs.text)
    print(rs.json())


# x = getWxAccessToken()
y = sendMsgAll()
