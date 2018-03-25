# -*- coding: utf-8 -*-
import scrapy


class QuoteLoginSpider(scrapy.Spider):
    name = 'quote_login'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        data={
            'csrf_token':token,
            'username':'abc',
            'password':'abc'
        }
        yield scrapy.FormRequest(url=self.start_urls[0],formdata=data,callback=self.parse_quote)

    def parse_quote(self, response):
        for q in response.css('div.quote'):
            author_name = q.css('small.author::text').extract_first()
            author_url = q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first()

            yield {'author_name': author_name, 'author_url': author_url}
