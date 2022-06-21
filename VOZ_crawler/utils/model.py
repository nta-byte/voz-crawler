from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from VOZ_crawler.utils.constants import DB_CONNECTION

Base = declarative_base()
Engine = create_engine(DB_CONNECTION)
