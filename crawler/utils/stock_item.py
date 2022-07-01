import re
from crawler.models.voz_stock_mapping import VOZStockMapping
from crawler.utils.logger import get_logger
logger = get_logger(name='StockItem')


class StockItemGenerator:
    def generate_items_from_comments(self, data, stockCodes):
        for item in data:
            for stockCode in list(set(stockCodes)):
                regText = '(\s%s$|\s%s\s)' % (stockCode, stockCode)
                content = item.content
                voz_commentid = item.id
                matched = re.search(regText, content, re.I)

                # if matched is None and item[1] is not None:
                #     matched = re.search(regText, item[1], re.I)

                if matched is not None:
                    newItem = {}
                    newItem['stock'] = stockCode
                    newItem['voz_commentid'] = voz_commentid
                    newItem['time'] = item.time
                    yield newItem
