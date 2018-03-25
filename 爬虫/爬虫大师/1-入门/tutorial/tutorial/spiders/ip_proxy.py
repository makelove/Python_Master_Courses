# -*- coding: utf-8 -*-
import scrapy, json
from scrapy import Request

from scrapy_redis.spiders import RedisSpider


# class IpProxySpider(scrapy.Spider):
class IpProxySpider(RedisSpider):
    name = 'ip_proxy'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/%s/']

    def start_requests(self):
        for i in range(1, 4):
            yield Request(self.start_urls[0] % i)

    def parse(self, response):
        for tr in response.xpath('//tbody/tr'):
            try:
                ip = tr.xpath('td[@data-title="IP"]/text()').extract()[0]
                port = tr.xpath('td[@data-title="PORT"]/text()').extract()[0]
                http_type = tr.xpath('td[@data-title="类型"]/text()').extract()[0].lower()
                # print(http_type,ip,port)
            except Exception as e:
                # print(e)
                continue

            #
            url = '%s://httpbin.org/ip' % http_type
            proxy = '%s://%s:%s' % (http_type, ip, port)

            meta = {
                'proxy': proxy,
                'dont_retry': True,
                'download_timeout': 10,
                #
                '_proxy_scheme': http_type,
                '_proxy_ip': ip,
                'port': port
            }
            yield Request(url, callback=self.check_available, meta=meta, dont_filter=True)

    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        if proxy_ip == json.loads(response.text)['origin']:
            yield {
                'proxy_scheme': response.meta['_proxy_scheme'],
                'proxy_ip': proxy_ip,
                'port': response.meta['port']
            }
