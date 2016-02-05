from .db import session
from .url import Url


def insert_data(data):
    #data = parsing(request_html('goo.gl/2kZ8TJ'), 'N=a:bls.title')
    try:
        session.query(Url).filter(url.classname == data['classname']).one()
    except NoResultFound:
        url = Url(classname=data['classname'], href=data['href'], 
                  title=data['title'])
        session.add(url)
        try:
            session.commit()
        except IntegrityError as exc:
            session.rollback()
