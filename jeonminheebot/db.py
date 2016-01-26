from flask import current_app, g
from alembic.config import Config
from alembic.environment import EnvironmentContext
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_engine():
    config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


def get_alembic_config(engine):
    if not isinstance(engine, Engine):
        raise Exception('jeonminheebot.db.get_alembic_config: engine is not'
                        '`Engine`')
    config = Config()
    config.set_main_option('script_location', '')
    config.set_main_option('sqlalchemy.url', str(engine.url))
    return config


def initialize_database(engine):
    return True


def get_database_revision(engine):
    config = get_alembic_config(engine)
    script = ScriptDirectory.from_config(config)
    result = [None]

    def get_revision(rev, context):
        result[0] = rev and script.get_revision(rev)
        return []
    with EnvironmentContext(config, script, fn=get_revision, 
                            as_sql=False, destination_rev=None, tag=None):
        script.run_env()
    return result[0]


def upgrade_database(engine, revision='head'):
    return True


def downgrade_database(engine, revision):
    return True


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


def close_db():
    return True


Base = declarative_base()
Session = sessionmaker(autocommit=True)
