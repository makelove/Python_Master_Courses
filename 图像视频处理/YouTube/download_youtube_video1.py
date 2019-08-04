# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 19:16
# @Author  : play4fun
# @File    : download_youtube_video1.py
# @Software: PyCharm

"""
download_youtube_video1.py:
在pythonanywhere下载所有 Scrapinghub频道的视频
https://www.youtube.com/channel/UCYb6YWTBfD0EB53shkN_6vA/videos?disable_polymer=1
"""

import os
from time import sleep

urls = ['https://www.youtube.com/watch?v=mw_Vo9m0l8o',
        'https://www.youtube.com/watch?v=EelmnSzykyI',
        'https://www.youtube.com/watch?v=G9Nni6G-iOc',
        'https://www.youtube.com/watch?v=VvFC93vAB7U',
        'https://www.youtube.com/watch?v=E6lOVwigsNA',
        'https://www.youtube.com/watch?v=J7IBwrehJ1s',
        'https://www.youtube.com/watch?v=qPvPiMbPSTE',
        'https://www.youtube.com/watch?v=sYtsqRr43PQ',
        'https://www.youtube.com/watch?v=vBuGnvF9xHg',
        'https://www.youtube.com/watch?v=Lo3aswJ7lzw',
        'https://www.youtube.com/watch?v=Wh0NbbL1WhE',
        'https://www.youtube.com/watch?v=ZxHbO_yD6PA',
        'https://www.youtube.com/watch?v=7PRy5LnTLaQ',
        'https://www.youtube.com/watch?v=wCKCmUpDZzQ',
        'https://www.youtube.com/watch?v=oMDYlXuPOag',
        'https://www.youtube.com/watch?v=QtZPVUmu3OA',
        'https://www.youtube.com/watch?v=vkA1cWN4DEc',
        'https://www.youtube.com/watch?v=JW_FxkSohkA',
        'https://www.youtube.com/watch?v=qjCtsHOC4J8',
        'https://www.youtube.com/watch?v=JYch0zRmcgU']

for url in urls[5:10]:
    print(url)
    cmd = 'youtube-dl  --write-auto-sub --sub-lang zh-Hans ' + url
    print(cmd)
    os.system(cmd)
    print('---------')
    sleep(5)
