# -*- coding: utf-8 -*-
import scrapy
from demo.items import FangItem
from scrapy_redis.spiders import RedisSpider

class FangSpider(RedisSpider):
    name = 'fang'
    #allowed_domains = ['fang.5i5j.com']
    #start_urls = ['https://fang.5i5j.com/bj/loupan/']
    redis_key = "fangspider:start_urls"

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(FangSpider, self).__init__(*args, **kwargs)
        
    def parse(self, response):
        #print(response.status)
        item = FangItem()
        item['title'] = response.selector.xpath("//title/text()")
        item['times'] = response.selector.xpath("//span[@class='pinfo']/text()")
        item['teacher'] = response.selector.xpath("//div[@class='professor_name']/a/text()")
        item['students'] = response.selector.xpath("//div[@class='forwho']/span[2]/text()")
        item['stu_num'] = response.selector.xpath("//span[@class='num']/text()")
        item['price'] = response.selector.xpath("//span[@class='money']/text()")
        item['topic'] = response.selector.xpath("//div[@class='J_outline_discribe_box']/span/text()")
        print(item)
        yield item
