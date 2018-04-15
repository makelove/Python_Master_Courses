# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 11:20
# @Author  : play4fun
# @File    : json_beautifulsoup1.py
# @Software: PyCharm

"""
json_beautifulsoup1.py:
"""

import json
from bs4 import BeautifulSoup# pip install bs4


jstext='''
{"MsgID":1065600378,"Type":49,"Time":1523587702,"SendWxid":"sidxxx","RecvWxid":"wxid_huasxxxxxo22","Msg":""}
'''

# js=json.loads(jstext,encoding='utf-8')
js=json.loads(jstext)
msgid=js['MsgID']
Times=js['Time']#时间戳
SendWxid=js['SendWxid']#发送者ID
RecvWxid=js['RecvWxid']#接受者ID
Msg=js['Msg']#消息主体
print(msgid,Times,SendWxid,RecvWxid)
print(f'在时间为{Times},{SendWxid}给{RecvWxid}发了一条消息，ID{msgid},内容为{Msg}')

Msg='<msg><appmsg appid="" sdkver=""><title><![CDATA[微信转账]]></title><des><![CDATA[收到转账0.10元。如需收钱，请点此升级至最新版本]]></des><action></action><type>2000</type><content><![CDATA[]]></content><url><![CDATA[https://support.weixin.qq.com/cgi-bin/mmsupport-bin/readtemplate?t=page/common_page__upgrade&text=text001&btn_text=btn_text_0]]></url><thumburl><![CDATA[https://support.weixin.qq.com/cgi-bin/mmsupport-bin/readtemplate?t=page/common_page__upgrade&text=text001&btn_text=btn_text_0]]></thumburl><lowurl></lowurl><extinfo></extinfo><wcpayinfo><paysubtype>1</paysubtype><feedesc><![CDATA[￥0.10]]></feedesc><transcationid><![CDATA[100005020118041300051321833195762448]]></transcationid><transferid><![CDATA[1000050201201804131400144912752]]></transferid><invalidtime><![CDATA[1523679502]]></invalidtime><begintransfertime><![CDATA[1523587702]]></begintransfertime><effectivedate><![CDATA[1]]></effectivedate><pay_memo><![CDATA[]]></pay_memo></wcpayinfo></appmsg></msg>'

so=BeautifulSoup(Msg,'xml')

title=so.msg.appmsg.title.contents[0]#消息标题
type1=so.msg.appmsg.type.contents[0]#消息类型
info=so.msg.appmsg.wcpayinfo

feed=info.feedesc.contents[0]#收到多少钱
transcationid=info.transcationid.contents[0]
transferid=info.transferid.contents[0]

print(title,type1,feed,transcationid,transferid)