from flask import current_app, g
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# alembic에 관련된 것도 추가할 것


def get_engine():
    config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


def get_alembic_config(engine):
    if not isinstance(engine, Engine):
        raise Exception('boilerplate.db.get_alembic_config: engine is not'
                        '`Engine`')
    config = Config()
    config.set_main_option('script_location', 'boilerplate:migrations')
    config.set_main_option('sqlalchemy.url', str(engine.url))
    return config


def get_session(engine=None):
    if engine is None:
        engine = get_engine()
    if hasattr(g, 'sess'):
        return g.sess
    session = Session(bind=engine)
    try:
        g.sess = session
    except RuntimeError:
        pass
    return session


def exist_data(data):
    return True


def insert_data():
    return True


def close_db():
    return True


Base = declarative_base()
Session = sessionmaker(autocommit=True)
