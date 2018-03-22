# -*- coding: utf-8 -*-
import scrapy
from .. import items
from time import time

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parse_product(self,response):
        item=items.Product()
        item['name'] = '某个产品'
        item['price'] = 43.343
        item['stock'] = 32
        item['last_updated'] = str(int(time()))
        yield item