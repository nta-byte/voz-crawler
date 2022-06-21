from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from VOZ_crawler.models.voz_spider import VOZSprider
from VOZ_crawler.utils.constants import DB_CONNECTION
engine = create_engine(DB_CONNECTION)
session = Session(engine)
o1 = VOZSprider(status='running')
session.add(o1)

o1.status = 'end'
session.add(o1)

session.commit()
print([x.__dict__ for x in session.query(VOZSprider).all()])
