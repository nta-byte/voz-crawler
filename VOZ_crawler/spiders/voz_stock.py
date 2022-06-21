from datetime import datetime
import pandas
from requests import session
import scrapy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import insert as pg_insert

from VOZ_crawler.items import VozCrawlerItem
from VOZ_crawler.models.voz_rawcomment import VOZRawComment
from VOZ_crawler.models.voz_stats import VOZStats
from VOZ_crawler.models.voz_stock_mapping import VOZStockMapping
from VOZ_crawler.models.voz_stock_stats import VOZStockStats
from VOZ_crawler.utils.constants import StockCodes

from VOZ_crawler.utils.logger import get_logger

from VOZ_crawler.utils.session import create_session
from VOZ_crawler.models import VOZLink, VOZSprider
from VOZ_crawler.utils.stock_item import StockItemGenerator

logger = get_logger('voz_stock')


class VozStockSpider(scrapy.Spider):
    name = 'voz_stock'
    allowed_domains = ['voz.vn']
    start_urls = [
        'https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528']

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
        item['content'] = comment.xpath(
            './/div[contains(@class, "message-userContent")]/article/div/text()').get()
        item['topic'] = comment.xpath(
            './/div[contains(@class, "message-userContent")]/article/div/blockquote/div[@class="bbCodeBlock-content"]/div/text()').get()
        item['time'] = comment.xpath('.//time/@datetime').get()
        item['id'] = comment.xpath('.//@data-content').get()
        item['author'] = comment.xpath('.//@data-author').get()
        item['spider_id'] = self.spiderRunner.id
        return item

    def spider_done(self):
        self.__commit_spider_runner_done()
        self.__generate_statis()
        self.__generate_report()
        self.status = 'end'

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

    def generate_stock_data(self):
        '''
        generate stock data from rawcomment
        Should run this script after spider done
        '''
        self.logger.info("start generate stock data")
        comments = self.session.query(VOZRawComment).filter_by(
            spider_id=self.spiderRunner.id).all()

        for item in StockItemGenerator().generate_items_from_comments(comments, StockCodes):
            self.add_voz_stock(item)
        self.logger.info("end generate stock data")

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
        self.spiderRunner.status = 'end'
        self.spiderRunner.time_end = datetime.utcnow()
        self.session.add(self.spiderRunner)
        self.session.commit()

    def __generate_statis(self):
        # generate general stats
        spider_id = self.__get_spider_id()
        num_rawcomment = self.session.query(func.count(VOZRawComment.id)).filter(
            VOZRawComment.spider_id == spider_id).first()[0]

        num_stock = self.session.query(func.count(VOZStockMapping.id)).filter(
            VOZStockMapping.spider_id == spider_id).first()[0]

        num_link = self.session.query(func.count(VOZLink.id)).filter(
            VOZLink.spider_id == spider_id).first()[0]
        stats = {}
        self.session.add(VOZStats(num_stock=num_stock,
                         num_rawcomment=num_rawcomment, num_link=num_link, spider_id=spider_id, stats=stats))
        self.session.commit()

        stockcodes = [tuple(x) for x in self.session.query(VOZStockMapping.stock).filter(
            VOZStockMapping.spider_id == spider_id).distinct().all()]
        stockStats = self.session.query(VOZStockMapping.stock, func.count(
            VOZStockMapping.stock)).filter(VOZStockMapping.stock.in_(stockcodes)).group_by(VOZStockMapping.stock).all()
        for x in stockStats:
            sql = pg_insert(VOZStockStats).values(stock=x[0], num=x[1], spider_id=spider_id).on_conflict_do_update(
                index_elements=['stock'], set_=dict(num=x[1], updated_at=datetime.utcnow(), spider_id=spider_id))
            self.session.execute(sql)
            self.session.commit()

    def __generate_report(self):
        stockStats = self.session.query(VOZStockStats).order_by(
            VOZStockStats.updated_at).filter(VOZStockStats.num >= 50).all()
        writer1 = pandas.ExcelWriter(
            f"data/voz_data-latest.xlsx")
        writer2 = pandas.ExcelWriter(
            f"data/voz_data-crawl-{datetime.utcnow().isoformat()}.xlsx")
        for stock in stockStats:
            data = self.session.query(VOZStockMapping).filter(
                VOZStockMapping.stock == stock.stock).order_by(VOZStockMapping.created_at).limit(50).all()
            df = pandas.DataFrame(
                [tuple([x.stock, x.voz_comment.topic, x.voz_comment.content,
                       x.voz_comment.time]) for x in data],
                columns=['Stock', 'Topic', 'Content', 'Time']
            )
            df.to_excel(writer1, sheet_name=stock.stock)
            df.to_excel(writer2, sheet_name=stock.stock)
        writer1.close()
        writer2.close()

    def __verify_link(self, url):
        rs = self.session.query(VOZLink).filter_by(link=url).first()
        if rs is None:
            self.session.add(VOZLink(link=url, spider_id=self.spiderRunner.id))
            self.session.commit()
            return True
        return False
