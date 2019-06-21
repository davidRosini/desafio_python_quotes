from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime)

from .meta import Base


class HistorySession(Base):
    __tablename__ = 'history_session'
    id = Column(Integer, primary_key=True)
    uuid = Column(Text)
    datetime = Column(DateTime)
    page = Column(Text)
