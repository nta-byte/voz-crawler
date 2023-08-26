from services.scrapy.crawler.utils.model import Base, Engine
from .voz_spider import VOZSprider
from .voz_link import VOZLink
from .voz_rawcomment import VOZRawComment
from .voz_stock_mapping import VOZStockMapping
from .voz_stats import VOZStats
from .voz_stock_stats import VOZStockStats

Base.metadata.create_all(Engine)
