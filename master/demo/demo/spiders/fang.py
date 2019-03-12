# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider,Rule  
from scrapy.linkextractors import LinkExtractor  
from demo.items import MasterItem  
import scrapy

class FangSpider(CrawlSpider):
    name = 'master'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['http://edu.csdn.net/courses/k/'] 
    item = MasterItem()
    
    page = 1
    def parse(self,response): 
        item = self.item
        urllist = response.selector.xpath('.//div[@class="course_dl_list"]//a[@target="_blank"]//@href')  
        for url in urllist:
            item['url'] = url.extract()
            yield item
        if self.page<=10:
            self.page += 1
        else:
            return
        next_url='http://edu.csdn.net/courses/k/p'+str(self.page)
        url = response.urljoin(next_url)#构建绝对url地址（可省略）
        yield scrapy.Request(url=url,callback=self.parse)
