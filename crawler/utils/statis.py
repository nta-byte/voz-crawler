from datetime import datetime

import pandas
from crawler.models import VOZSprider, VOZRawComment, VOZStockMapping
from crawler.models.voz_link import VOZLink
from crawler.models.voz_stats import VOZStats
from crawler.models.voz_stock_stats import VOZStockStats
from crawler.utils.constants import MAX_STOCKMAPPING_INSERT, StockCodes
from crawler.utils.logger import get_logger
from crawler.utils.session import create_session
from crawler.utils.stock_item import StockItemGenerator
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy import func


class StatisStock:
    def __init__(self) -> None:
        self.session = create_session()
        self.spiders = self.session.query(
            VOZSprider).filter_by(status='crawled').all()
        self.logger = get_logger('voz_stockmapping')

    def run(self):
        for spider in self.spiders:
            self.logger.info("start thread")
            self.logger.info("start generate stock data spiderid=%s time_start=%s time_end=%s" % (
                spider.id, spider.time_start, spider.time_end))
            rawcomments = self.session.query(VOZRawComment).filter_by(
                spider_id=spider.id).all()

            self.session.query(VOZStockMapping).filter_by(
                spider_id=spider.id).delete(synchronize_session=False)

            self.logger.info("total=%s" % (len(rawcomments)))

            idx = 1
            list = []
            for item in StockItemGenerator().generate_items_from_comments(rawcomments, StockCodes):
                self.logger.info("stockmapping: adding ... %s: %s - %s " %
                                 (idx, item['voz_commentid'], item['stock']))
                item['spider_id'] = spider.id
                list.append(item)
                if len(list) >= MAX_STOCKMAPPING_INSERT:
                    self.__add_stockmapping(list)
                    list = []
                idx += 1

            self.__add_stockmapping(list)
            self.__generate_voz_statis(spider_id=spider.id)
            spider.status = 'ended'
            self.session.add(spider)
            self.session.commit()
            self.logger.info("end generate stock data")
        self.__generate_report()

    def __add_stockmapping(self, list):
        if len(list) > 0:
            sql = pg_insert(VOZStockMapping).values(
                list).on_conflict_do_nothing(index_elements=['voz_commentid'])
            self.session.execute(sql)
            self.session.commit()

    def __generate_voz_statis(self, spider_id):
        self.session.query(VOZStats).filter_by(
            spider_id=spider_id).delete(synchronize_session=False)

        self.session.query(VOZStockStats).filter_by(
            spider_id=spider_id).delete(synchronize_session=False)

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
            f"crawler/data/voz_data-latest.xlsx")
        writer2 = pandas.ExcelWriter(
            f"crawler/data/voz_data-crawl-{datetime.utcnow().isoformat()}.xlsx")
        for stock in stockStats:
            data = self.session.query(VOZStockMapping).filter(
                VOZStockMapping.stock == stock.stock).order_by(VOZStockMapping.created_at).limit(50).all()
            df = pandas.DataFrame(
                [tuple([x.voz_comment.topic, x.voz_comment.content,
                        x.voz_comment.time]) for x in data],
                columns=['Topic', 'Content', 'Time']
            )
            df.to_excel(writer1, sheet_name=stock.stock,)
            df.to_excel(writer2, sheet_name=stock.stock)
        writer1.close()
        writer2.close()
