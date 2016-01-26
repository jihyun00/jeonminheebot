from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'Url',

class Url(Base):

    url_id = Column(Integer, primary_key=True) 

    link = Column(String)

    __tablename__ = 'url'
