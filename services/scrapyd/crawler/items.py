# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VozCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    topic = scrapy.Field()
    content = scrapy.Field()
    spider_id = scrapy.Field()
