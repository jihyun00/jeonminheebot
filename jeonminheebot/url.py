from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'Url',


class Url(Base):

    url_id = Column(Integer, primary_key=True)

    classname = Column(String, unique=True, nullable=False)

    href = Column(String, nullable=False)

    title = Column(String, nullable=False)

    __tablename__ = 'url'
