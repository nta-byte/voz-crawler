from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import JSONB

from VOZ_crawler.utils.model import Base


class VOZStats(Base):
    __tablename__ = 'voz_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    num_stock = Column(Integer)
    num_rawcomment = Column(Integer)
    num_link = Column(Integer)
    stats = Column(JSONB)
    spider_id = Column(Integer, ForeignKey(
        'voz_spider.id', ondelete='cascade'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
