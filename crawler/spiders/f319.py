from datetime import datetime
from requests import session
import scrapy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert as pg_insert

from crawler.items import VozCrawlerItem
from crawler.models.voz_rawcomment import VOZRawComment
from crawler.models.voz_stats import VOZStats
from crawler.models.voz_stock_mapping import VOZStockMapping
from crawler.models.voz_stock_stats import VOZStockStats
from crawler.utils.constants import StockCodes

from crawler.utils.logger import get_logger

from crawler.utils.session import create_session
from crawler.models import VOZLink, VOZSprider
from crawler.utils.stock_item import StockItemGenerator

logger = get_logger('voz_stock')


class VozStockSpider(scrapy.Spider):
    name = 'f319_stock'
    allowed_domains = ['f319.com']
    start_urls = [
        'https://f319.com/'
    ]

    first_time = True
    session = create_session()

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.status = "starting"
        self.count = 0
        self.__start_new_thread()

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
                yield self.process_item(comment)

            next_page_url = response.xpath(
                '//a[contains(@class, "pageNav-jump--prev")]/@href').get()
            if next_page_url is not None and self.__verify_link(next_page_url):
                yield scrapy.Request(response.urljoin(next_page_url))
            else:
                print("DONE")

    def process_item(self, comment):
        item = VozCrawlerItem()
        content = comment.xpath('.//div[contains(@class, "messageContent")]/article//text()').extract()
        _content = [line for line in content if line != "\n"]
        item['content'] = ''.join(_content)
        topic = comment.xpath(
            './/div[contains(@class, "messageContent")]/article/div/blockquote/div[@class="bbCodeBlock-content"]/div/text()').extract()
        item['topic'] = ''.join([line for line in topic if line != "\n"])
        item['time'] = comment.xpath('.//time/@datetime').get()
        item['id'] = comment.xpath('.//@data-content').get()
        item['author'] = comment.xpath('.//@data-author').get()
        item['spider_id'] = self.spiderRunner.id
        return item

    def spider_done(self):
        self.__commit_spider_runner_done()

    def spider_error_rollback(self, reason=''):
        '''
        delete all data in this state
        '''
        print(
            f"spider rollback action: remove spider id={self.spiderRunner.id}")
        self.status = 'error'
        self.spiderRunner.status = 'error'
        self.spiderRunner.reason = reason
        self.session.add(self.spiderRunner)
        self.session.commit()

        # delete VOZRawComment
        self.session.query(VOZRawComment).filter(
            VOZRawComment.spider_id == self.__get_spider_id()).delete()
        self.session.commit()

        # delete VOZRawComment
        self.session.query(VOZLink).filter(
            VOZLink.spider_id == self.__get_spider_id()).delete()
        self.session.commit()

        # delete VOZRawComment
        self.session.query(VOZStockMapping).filter(
            VOZStockMapping.spider_id == self.__get_spider_id()).delete()
        self.session.commit()
        self.close(self, reason)

    def add_voz_stock(self, item):
        item['spider_id'] = self.spiderRunner.id
        sql = pg_insert(VOZStockMapping).values(
            **item).on_conflict_do_nothing(index_elements=['voz_commentid'])
        self.session.execute(sql)
        self.session.commit()

    def add_rawcomment(self, item):
        item['spider_id'] = self.spiderRunner.id
        sql = pg_insert(VOZRawComment).values(
            **item).on_conflict_do_nothing(index_elements=['id'])
        self.session.execute(sql)
        self.session.commit()

    # INTERNAL FUNC
    def __start_new_thread(self):
        vozSpider = VOZSprider(status='running')
        self.session.add(vozSpider)
        self.session.flush()
        self.session.commit()
        self.spiderRunner = vozSpider

    def __get_spider_id(self):
        return self.spiderRunner.id

    def __commit_spider_runner_done(self):
        self.spiderRunner.status = 'crawled'
        self.spiderRunner.time_end = datetime.utcnow()
        self.session.add(self.spiderRunner)
        self.session.commit()

    def __verify_link(self, url):
        rs = self.session.query(VOZLink).filter_by(link=url).first()
        if rs is None:
            self.session.add(VOZLink(link=url, spider_id=self.spiderRunner.id))
            self.session.commit()
            return True
        return False
