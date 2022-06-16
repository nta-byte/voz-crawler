import scrapy

from VOZ_crawler.items import VozCrawlerItem
import re
import logging

logger = logging.getLogger(name='VOZ')


class VozStockSpider(scrapy.Spider):
    name = 'voz_stock'
    allowed_domains = ['voz.vn']
    start_urls = [
        'https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528']

    first_time = True
    count = 0

    stockCodes = [
        'HPG',
        'POW',
        'SSI',
        'MBB',
        'STB',
        'VPB',
        'TCH',
        'TCB',
        'VHM',
        'TPB',
        'NVL',
        'HDB',
        'CTG',
        'VNM',
        'MWG',
        'VRE',
        'GAS',
        'SBT',
        'VIC',
        'FPT',
        'BID',
        'PNJ',
        'VCB',
        'REE',
        'BVH',
        'KDH',
        'MSN',
        'PLX',
        'VJC',
        'CTR'
    ]

    priorities = {}

    num_completed = 0

    maxItemInStock = 50

    def parse(self, response):
        if self.first_time:
            self.first_time = False
            newPage = scrapy.Selector(response).xpath(
                '//ul[@class="pageNav-main"]/li[last()]/a/@href').get()
            yield scrapy.Request(response.urljoin(newPage))
        else:
            comments = scrapy.Selector(response).xpath(
                '//article[contains(@class, "js-post")]')
            for comment in comments[::-1]:
                item = VozCrawlerItem()
                item['Content'] = comment.xpath(
                    './/div[contains(@class, "message-userContent")]/article/div/text()').get()
                item['Topic'] = comment.xpath(
                    './/div[contains(@class, "message-userContent")]/article/div/blockquote/div[@class="bbCodeBlock-content"]/div/text()').get()
                item['Time'] = comment.xpath('.//time/@datetime').get()
                for stockCode in self.stockCodes:
                    if stockCode not in self.priorities.keys():
                        logger.info("new stock: %s " % stockCode)
                        self.priorities[stockCode] = 0

                    if self.priorities[stockCode] >= self.maxItemInStock:
                        continue
                    regText = '(%s$|%s\s)' % (stockCode, stockCode)
                    matched = re.search(regText, item['Content'], re.I)
                    if matched is None and item['Topic'] is not None:
                        matched = re.search(regText, item['Topic'], re.I)
                    if matched is not None:
                        item['Code'] = stockCode
                        self.priorities[stockCode] += 1
                        if self.priorities[stockCode] == self.maxItemInStock:
                            logger.info("done stock: %s" % stockCode)
                            self.num_completed += 1
                            logger.info("total stock done: %d" %
                                        self.num_completed)

                        yield item

            next_page_url = response.xpath(
                '//a[contains(@class, "pageNav-jump--prev")]/@href').get()
            if next_page_url is not None or self.num_completed >= len(self.stockCodes):
                yield scrapy.Request(response.urljoin(next_page_url))
            else:
                logger.info("stats: %s" % self.priorities)
                print("DONE")
