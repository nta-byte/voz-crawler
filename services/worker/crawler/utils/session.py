from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from services.worker.crawler.utils.constants import DB_CONNECTION


def create_session():
    engine = create_engine(DB_CONNECTION)
    session = Session(engine)
    return session
