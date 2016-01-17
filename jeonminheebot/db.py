from flask import current_app
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine():
    config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


def exist_data(data):
    return True


def insert_data():
    return True


def close_db():
    return True
