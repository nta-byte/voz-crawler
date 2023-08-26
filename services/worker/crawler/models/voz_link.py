from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from services.worker.crawler.utils.model import Base


class VOZLink(Base):
    __tablename__ = 'voz_link'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, unique=True)
    spider_id = Column(Integer, ForeignKey(
        'voz_spider.id', ondelete='cascade'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
