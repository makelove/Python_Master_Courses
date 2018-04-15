# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 11:00
# @Author  : play4fun
# @File    : t1.py
# @Software: PyCharm

"""
t1.py:
"""

import xml.etree.ElementTree as ET

msg='''<msg><appmsg appid="" sdkver=""><title><![CDATA[微信转账]]></title><des><![CDATA[收到转账0.10元。如需收钱，请点此升级至最新版本]]></des><action></action><type>2000</type><content><![CDATA[]]></content><url><![CDATA[https://support.weixin.qq.com/cgi-bin/mmsupport-bin/readtemplate?t=page/common_page__upgrade&text=text001&btn_text=btn_text_0]]></url><thumburl><![CDATA[https://support.weixin.qq.com/cgi-bin/mmsupport-bin/readtemplate?t=page/common_page__upgrade&text=text001&btn_text=btn_text_0]]></thumburl><lowurl></lowurl><extinfo></extinfo><wcpayinfo><paysubtype>1</paysubtype><feedesc><![CDATA[￥0.10]]></feedesc><transcationid><![CDATA[100005020118041300051321833195762448]]></transcationid><transferid><![CDATA[1000050201201804131400144912752]]></transferid><invalidtime><![CDATA[1523679502]]></invalidtime><begintransfertime><![CDATA[1523587702]]></begintransfertime><effectivedate><![CDATA[1]]></effectivedate><pay_memo><![CDATA[]]></pay_memo></wcpayinfo></appmsg></msg>'''

et=ET.fromstring(msg)
