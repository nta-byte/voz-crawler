from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from services.scrapy.crawler.utils.model import Base


class VOZStockStats(Base):
    __tablename__ = 'voz_stock_stats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock = Column(String, nullable=False, unique=True)
    num = Column(Integer, nullable=False)
    spider_id = Column(Integer, ForeignKey(
        'voz_spider.id', ondelete='cascade'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
