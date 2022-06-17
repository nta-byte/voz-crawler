import logging
import re
import sys


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
logger.addHandler(stdout_handler)


class StockItem:
    def generate_items(self, data, stockCodes):
        for item in data:
            for stockCode in list(set(stockCodes)):
                regText = '(%s$|%s\s)' % (stockCode, stockCode)
                content = item[4]
                voz_rawcomment = item[0]
                matched = re.search(regText, content, re.I)

                # if matched is None and item[1] is not None:
                #     matched = re.search(regText, item[1], re.I)

                if matched is not None:
                    newItem = {}
                    newItem['stock'] = stockCode
                    newItem['voz_rawcomment'] = voz_rawcomment
                    yield newItem
