# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import BooksItem


# class BooksSpider(scrapy.Spider):
class BooksSpider(RedisSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def __init__(self):
        self.counter = 0

    def parse(self, response):
        # if self.counter > 2:
        #     return
        # else:
        #     self.counter += 1

        for book in response.css('article.product_pod'):
            try:
                bname = book.xpath('./h3/a/@title').extract_first()
                price = book.css('p.price_color::text').extract()[0]
                # yield {'name': bname, 'price': price}

                bookit = BooksItem()
                bookit['name'] = bname
                bookit['price'] = price
                yield bookit

            except Exception as e:
                print(e)

        #
        next_url = response.css('li.next a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
