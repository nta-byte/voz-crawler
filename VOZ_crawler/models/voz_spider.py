from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

from VOZ_crawler.utils.model import Base


class VOZSprider(Base):
    __tablename__ = 'voz_spider'
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, default='start')
    reason = Column(String, default='')
    time_start = Column(DateTime, default=datetime.utcnow)
    time_end = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
