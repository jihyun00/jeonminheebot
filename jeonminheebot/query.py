from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from .db import session
from .url import Url


def insert_data(data):
    # data = parsing(request_html('goo.gl/2kZ8TJ'), 'N=a:bls.title')
    try:
        session.query(Url).filter(Url.classname == data['classname']).one()
    except NoResultFound:
        url = Url(classname=data['classname'], href=data['href'],
                  title=data['title'])
        session.add(url)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
