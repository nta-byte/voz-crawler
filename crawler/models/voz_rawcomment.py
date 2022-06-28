from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String, create_engine
from crawler.utils.model import Base


class VOZRawComment(Base):
    __tablename__ = 'voz_rawcomment'
    id = Column(String, primary_key=True)
    time = Column(DateTime, nullable=False)
    author = Column(String)
    topic = Column(String)
    content = Column(String)
    spider_id = Column(Integer, ForeignKey(
        'voz_spider.id', ondelete='cascade'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
