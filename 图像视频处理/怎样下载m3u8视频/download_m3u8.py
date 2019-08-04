# -*- coding: utf-8 -*-
# @Time    : 2019-07-15 19:22
# @Author  : play4fun
# @File    : download_m3u8.py
# @Software: PyCharm

"""
download_m3u8.py:

下载m3u8视频，并合并

https://github.com/globocom/m3u8
pip install m3u8

"""
import sys
import requests
from urllib.request import urlretrieve
import m3u8
from random import randint
from os import system
import os


def main(url):
    m = m3u8.load(url)
    #
    print('请输入序号，你想看哪个清晰度:')
    for i, pl in enumerate(m.playlists):
        print(f"{i}:{pl.stream_info.resolution}")
    indexs: str = input('请输入序号，你想看哪个清晰度(默认720p-2):')
    indexs = '2' if indexs == '' else indexs
    if indexs.isnumeric():
        idx = int(indexs)
        pl = m.playlists[idx]
        m2 = m3u8.load(pl.absolute_uri)
        print('开始下载 ts列表...')
        for sm in m2.segments:
            url2 = sm.absolute_uri
            print(url2)
            urlretrieve(url2, sm.uri)
        print('下载完毕')

        # 合并ts片段，存为与文件夹同名的ts文件
        print('开始合并文件:')
        fn = input('输入文件名:')
        fn = f"{randint(1000, 9999)}" if fn == '' else fn
        fn = fn + '.mp4'

        with open(fn, 'wb') as f:
            for sm in m2.segments:
                # file_path = os.path.join(directory, f'{n}.ts')
                with open(sm.uri, 'rb') as g:
                    f.write(g.read())
        print('合并文件完毕。。。')

        #
        cmds = f'/Applications/IINA.app/Contents/MacOS/iina-cli ' + fn
        input(f'打开？{cmds}')  # TODO
        system(cmds)

    pass


def merge_file():
    l1 = [int(f[:-3]) for f in os.listdir() if f.endswith('.ts')]
    l1 = sorted(l1)

    fn = f"{randint(1000, 9999)}"
    fn = fn + '.mp4'
    with open(fn, 'wb') as f:
        for fp in l1:
            print(fp, f"{fp}.ts")
            with open(f"{fp}.ts", 'rb') as g:
                f.write(g.read())
    print('合并文件完毕。。。')


def main2(url):
    # 获取m3u8
    resp = requests.get(url)
    # print(resp.text)
    '''
    #EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=460800, RESOLUTION=480x270
/asp/hls/450/0303000a/3/default/1eb4c564098544008dc19416eb7990f2/450.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=870400, RESOLUTION=640x360
/asp/hls/850/0303000a/3/default/1eb4c564098544008dc19416eb7990f2/850.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=1228800, RESOLUTION=1280x720
/asp/hls/1200/0303000a/3/default/1eb4c564098544008dc19416eb7990f2/1200.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=2048000, RESOLUTION=1280x720
/asp/hls/2000/0303000a/3/default/1eb4c564098544008dc19416eb7990f2/2000.m3u8
    '''
    m3u8s = []  # 列表
    for sp in resp.text.split('#'):
        sp2 = sp.split('\n')
        sp2 = [x for x in sp2 if x != '']
        # print(len(sp2))

    pass


if __name__ == '__main__':

    if len(sys.argv) == 2:
        url = sys.argv[1]

        main(url)
        # merge_file()
    else:
        print('python download_m3u8.py m3u8_url')
