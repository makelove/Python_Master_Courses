# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

import json


class MusicSpider(scrapy.Spider):
    name = 'music_phone'
    # allowed_domains = ['music.baidu.com']
    start_urls = ['http://music.baidu.com/search/%E6%88%91%E7%9A%84%E7%A5%96%E5%9B%BD']
    songlink_url = 'http://musicapi.qianqian.com/v1/restserver/ting?from=webapp_music&method=baidu.ting.song.playAAC&format=jsonp&songid='

    def parse(self, response):
        for songid in response.xpath('//li/@data-sid').extract():
            print('songIds:', songid)
            url=self.songlink_url+songid

            yield Request(url,callback=self.parse_song)
            # break

    def parse_song(self, response):
        # print(response.text)
        js = json.loads(response.text)
        try:
            songLink = js["bitrate"]["file_link"]
            songName = js["songinfo"]["title"]
            artistName = js["songinfo"]["author"]

        except:
            return
        if songLink == '':
            return

        yield {'artistName': artistName, 'songName': songName, 'songLink': songLink}
