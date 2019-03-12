# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):
    # define the fields for your item here like:
    title    = scrapy.Field()
    times    = scrapy.Field()
    teacher  = scrapy.Field()
    students = scrapy.Field()
    stu_num  = scrapy.Field()
    price    = scrapy.Field()
    topic    = scrapy.Field()
    #pass
