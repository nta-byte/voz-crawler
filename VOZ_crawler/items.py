# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VozCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Code = scrapy.Field()
    Time = scrapy.Field()
    Topic = scrapy.Field()
    Content = scrapy.Field()
    pass
