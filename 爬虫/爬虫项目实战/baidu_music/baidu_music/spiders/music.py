# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

import json


class MusicSpider(scrapy.Spider):
    name = 'music'
    # allowed_domains = ['music.baidu.com']
    start_urls = ['http://music.baidu.com/search?fr=ps&ie=utf-8&key=童话镇']
    songlink_url = 'http://play.baidu.com/data/music/songlink'

    def parse(self, response):
        for songid in response.xpath('//a/@href').re('/song/(\d+)'):
            print('songIds:', songid)
            data = {'songIds': songid}  # 257524668
            yield FormRequest(url=self.songlink_url, formdata=data, callback=self.parse_song)
            # break

    def parse_song(self, response):
        # print(response.text)
        js = json.loads(response.text)
        try:
            songName = js['data']['songList'][0]['songName']
            artistName = js['data']['songList'][0]['artistName']
            songLink = js['data']['songList'][0]['songLink']
        except:
            return
        if songLink == '':
            return

        yield {'artistName': artistName, 'songName': songName, 'songLink': songLink}
