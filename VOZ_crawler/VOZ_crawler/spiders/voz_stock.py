import scrapy

from VOZ_crawler.items import VozCrawlerItem
import re


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
        'PDR',
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
    ]

    priorities = {}

    num_completed = 0

    def parse(self, response):
        if self.first_time:
            self.first_time = False
            newPage = scrapy.Selector(response).xpath(
                '//ul[@class="pageNav-main"]/li[last()]/a/@href').get()
            yield scrapy.Request(response.urljoin(newPage))
        else:
            self.count += 1
            comments = scrapy.Selector(response).xpath(
                '//div[contains(@class, "js-messageContent")]')
            for comment in comments[::-1]:
                item = VozCrawlerItem()
                item['Content'] = comment.xpath(
                    'div[contains(@class, "message-userContent")]/article/div/text()').get()
                item['Topic'] = comment.xpath(
                    'div[contains(@class, "message-userContent")]/article/div/blockquote/div[@class="bbCodeBlock-content"]/div/text()').get()
                for stockCode in self.stockCodes:
                    if stockCode is not self.priorities:
                        self.priorities[stockCode] = 0

                    if self.priorities[stockCode] >= 50:
                        continue

                    matched = re.search(stockCode, item['Content'], re.I)
                    if matched is not None:
                        item['Code'] = stockCode
                        self.priorities[stockCode] += 1
                        if self.priorities[stockCode] == 50:
                            self.num_completed += 1
                        yield item

            next_page_url = response.xpath(
                '//a[contains(@class, "pageNav-jump--prev")]/@href').get()
            if next_page_url is not None or self.num_completed >= 30:
                yield scrapy.Request(response.urljoin(next_page_url))
