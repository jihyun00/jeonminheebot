from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from .db import Base, session


__all__ = 'Url',


class Url(Base):

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)

    href = Column(String, nullable=False)

    __tablename__ = 'url'

    def create(self, url_data):
        try:
            self.title = url_data['title']
            self.href = url_data['href']
            session.query(Url) \
                   .filter(Url.classname == self.classname).one()
        except NoResultFound:
            session.add(self)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
