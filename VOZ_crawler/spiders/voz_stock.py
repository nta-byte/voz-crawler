import sys
import scrapy

from VOZ_crawler.items import VozCrawlerItem
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',
                              '%m-%d-%Y %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class VozStockSpider(scrapy.Spider):
    name = 'voz_stock'
    allowed_domains = ['voz.vn']
    start_urls = [
        'https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528']

    first_time = True

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
                yield item

            next_page_url = response.xpath(
                '//a[contains(@class, "pageNav-jump--prev")]/@href').get()
            if next_page_url is not None:
                yield scrapy.Request(response.urljoin(next_page_url))
            else:
                logger.info("stats: %s" % self.priorities)
                print("DONE")
