import re
import sys
import pandas as pd
from sqlalchemy import create_engine
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
logger.addHandler(stdout_handler)


conn_string = 'postgresql://postgres:abcd1234@0.0.0.0:2345/postgres'
db = create_engine(conn_string)
conn = db.connect()


def save_db():
    df.to_sql('voz_all_comment', con=conn, if_exists='replace')


def generate_item():
    stockCodes = [
        'ROS', 'VHM', 'ITA', 'BID', 'HNG', 'FPT', 'APH', 'MSB', 'HPG', 'HAI', 'GEX', 'VNM', 'ART', 'VCG', 'FLC', 'STB', 'VPB', 'VRE', 'AAA', 'ASM', 'BSR', 'KLF', 'MBB', 'TCB', 'HAG', 'VIC', 'BCG', 'DXG', 'CTG', 'APS', 'SSI', 'TPB', 'POW', 'HVN'
    ]
    priorities = {}
    num_completed = 0
    maxItemInStock = 50
    for item in df.to_numpy():
        for stockCode in list(set(stockCodes))[0:30]:
            if stockCode not in priorities.keys():
                logger.info("new stock: %s " % stockCode)
                priorities[stockCode] = 0

            if priorities[stockCode] >= maxItemInStock:
                continue
            regText = '(%s$|%s\s)' % (stockCode, stockCode)
            matched = re.search(regText, item[0], re.I)
            if matched is None and item[1] is not None:
                matched = re.search(regText, item[1], re.I)
            if matched is not None:
                newItem = {}
                newItem['code'] = stockCode
                newItem['content'] = item[0]
                newItem['topic'] = item[1]
                newItem['time'] = item[2]
                priorities[stockCode] += 1
                if priorities[stockCode] == maxItemInStock:
                    logger.info("done stock: %s" % stockCode)
                    num_completed += 1
                    logger.info("total stock done: %d" %
                                num_completed)

                yield newItem
    logger.info('statis: total=%s \n data=%s \n codes=%s' %
                (len(priorities), priorities, priorities.keys()))

    itemOver50 = list(filter(lambda x: x[1] >= 50, priorities.items()))

    logger.info('statis >= 50: total=%s \n data=%s' %
                (len(itemOver50), list(map(lambda x: x[0], itemOver50))))


def filter_stock():
    data_arr = list()
    for item in generate_item():
        data_arr.append(item)
    voz_comments_df = pd.DataFrame(data_arr)
    voz_comments_df.to_sql(
        "voz_comment", con=conn, if_exists='replace')
    voz_comments_df.to_csv(r"data/comments.csv", index=None, encoding='utf-8')
    voz_comments_df.to_excel(r"data/comments.xlsx", index=None,
                             encoding='utf-8', sheet_name='VOZ')


df = pd.read_json("data/comments-all-latest.json", encoding='utf-8')

save_db()
filter_stock()
