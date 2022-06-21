# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class VozCrawlerCompleteMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(
            s.spider_end, signal=signals.stats_spider_closed)

        crawler.signals.connect(
            s.handle_spider_error, signal=signals.spider_error)
        return s

    def handle_spider_error(self, failure, response, spider):
        spider.logger.error(
            f"t=handle_spider_error, msg={failure.getErrorMessage()}")
        spider.spider_error_rollback(reason=failure.getErrorMessage())

    def spider_end(self, spider):
        try:
            spider.logger.info('Spider closed: %s' % spider.name)
            if spider.status == 'error':
                return False

            # generate new data for stock comment
            spider.generate_stock_data()

            # done spider
            spider.spider_done()

        except Exception as e:
            print(e)
            spider.spider_error_rollback(reason=str(e))

        # topStocks = client.get_top_stock()
        # array = []
        # for stock in topStocks:
        #     rs = client.query(QueryGetStockInfo % stock[0]).fetchall()
        #     array += rs

        # # call done action

        # # generate_csv
        # df2 = pandas.DataFrame.from_records(array)
        # df2.to_csv(r"data/comments.csv",
        #            index=None, encoding='utf-8')
        # df2.to_excel(r"data/comments.xlsx", index=None,
        #              encoding='utf-8', sheet_name='VOZ')
