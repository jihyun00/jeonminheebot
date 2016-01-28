from flask import current_app, g
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as SqlalchemySession, sessionmaker


def get_engine() -> Engine:
    config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


def get_alembic_config(engine) -> Config:
    if not isinstance(engine, Engine):
        raise Exception('jeonminheebot.db.get_alembic_config: engine is not'
                        '`Engine`')
    config = Config()
    config.set_main_option('script_location', 'jeonminheebot:migrations')
    config.set_main_option('sqlalchemy.url', str(engine.url))
    return config


def initialize_database(engine):
    return True


def get_database_revision(engine):
    return True


def upgrade_database(engine, revision='head'):
    return True


def downgrade_database(engine, revision):
    return True


def get_session(engine=None) -> SqlalchemySession:
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


def close_db():
    return True


Base = declarative_base()
Session = sessionmaker()
