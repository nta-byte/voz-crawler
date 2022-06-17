from VOZ_crawler.utils.constants import TableVOZRawComment, TableVOZStockComment


CreateVOZRawComment = '''
  create table if not exists voz_rawcomment(
    id varchar(45) not null PRIMARY KEY,
    author varchar(100),
    time timestamp,
    topic varchar,
    content varchar
);
'''

CreateVOZLink = '''
 create table if not exists voz_link(
                id  SERIAL PRIMARY KEY,
                link varchar(100)
            );
'''


CreateVOZStockComment = '''
  create table if not exists voz_stockcomment(
            id  SERIAL PRIMARY KEY,
            stock varchar(100),
            voz_rawcomment varchar(45) not null,
            CONSTRAINT fk_voz_rawcomment
            FOREIGN KEY(voz_rawcomment)
            REFERENCES voz_rawcomment(id)
            ON DELETE CASCADE,
            UNIQUE(stock, voz_rawcomment)
        );
'''


QueryGetTop30Stock = '''
select vs.stock, count(vs.stock) num from voz_stockcomment vs group by vs.stock having count(vs.stock) >=50 order by num desc limit 30;
'''

QueryCountVOZStockCOmment = f'''
select count(*) from {TableVOZStockComment}
'''

QueryGetStockInfo = f'''
select tc.stock, rc.topic, rc.content, rc.time from {TableVOZStockComment} tc 
inner join {TableVOZRawComment} rc on rc.id = tc.voz_rawcomment
where tc.stock=\'%s\'
order by rc.time desc
limit 50
'''
