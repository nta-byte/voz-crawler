import psycopg2
from VOZ_crawler.utils.constants import TableVOZStockComment
from VOZ_crawler.utils.queries import CreateVOZLink, CreateVOZRawComment, CreateVOZStockComment, QueryCountVOZStockCOmment, QueryGetTop30Stock


class PYPG:

    def __init__(self):
        self.conn = psycopg2.connect(self.__get_conn_str())
        self.excute_query(CreateVOZRawComment)
        self.excute_query(CreateVOZLink)
        self.excute_query(CreateVOZStockComment)

    def __get_conn_str(self):
        return 'postgresql://postgres:abcd1234@0.0.0.0:2345/postgres'

    def excute_query(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def query(self, sql, ):
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur

    def voz_link_insert(self, item):
        self.insert_item('voz_link', item=item)

    def voz_rawcomment_insert(self, item):
        self.insert_item('voz_rawcomment', item=item, onconflicts=[
            ('voz_rawcomment_pkey', 'do nothing')
        ])

    def verify_link(self, link):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT count(*) from voz_link where link='%s'" % link)
        rs = cur.fetchone()
        if rs[0] == 0:
            self.voz_link_insert({'link': link})
            return True
        return False

    def get_all_rawcomment(self):
        cur = self.conn.cursor()
        cur.execute(QueryCountVOZStockCOmment)
        limit = 100000000
        # if cur.fetchone()[0] > 0:
        #     limit = 500

        cur.execute(
            f"SELECT * from voz_rawcomment order by id limit {limit};")
        return cur.fetchall()

    def get_top_stock(self):
        cur = self.conn.cursor()
        cur.execute(QueryGetTop30Stock)
        return cur.fetchall()

    def get_stock_over_50(self):
        cur = self.conn.cursor()
        cur.execute(
            "select vs.stock, count(vs.stock) num from voz_stockcomment vs group by vs.stock having count(vs.stock) >=50 order by num desc;" % (TableVOZStockComment))
        return cur.fetchall()

    def voz_stockcomment_insert(self, item):
        self.insert_item('voz_stockcomment', item=item, onconflicts=[
            ('voz_stockcomment_stock_voz_rawcomment_key', 'do nothing')
        ])

    def truncate(self, tableName):
        self.conn.cursor().execute('''
        truncate %s;
        ''' % tableName)
        self.conn.commit()

    def insert_item(self, tableName, item=None, onconflicts=None):
        sql = "insert into "+tableName+"(" + \
            ','.join([x.lower() for x in item.keys()]) + \
            ") VALUES (" + ",".join(["%s"]*len(item.keys())
                                    ) + ")"

        if onconflicts is not None and len(onconflicts) > 0:
            sql += ''.join([" ON CONFLICT ON CONSTRAINT %s %s " %
                            onconflict for onconflict in onconflicts])

        self.conn.cursor().execute(sql, tuple(item.values()))
        self.conn.commit()

    def close(self):
        self.conn.close()
