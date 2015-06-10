# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PpjstaffItem(scrapy.Item):
    bil = scrapy.Field()
    nama = scrapy.Field()
    jawatan = scrapy.Field()
    gelaran = scrapy.Field()
    ext = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
