import functools
import os
import tempfile

from flask import g
from pytest import fixture
from sqlalchemy import create_engine

from jeonminheebot.db import Base, Session
from jeonminheebot.app import app


TEST_DATABASE_URL = 'sqlite:///jb.db'


def pytest_addoption(parser):
    parser.addoption("--real", action="store_true",
                     help="real request")


def get_engine():
    url = app.config['DATABASE_URL'] = TEST_DATABASE_URL
    engine = create_engine(url)
    app.config['DATABASE_ENGINE'] = engine
    return engine


@fixture
def f_session(request):
    with app.test_request_context() as _ctx:
        engine = get_engine()
        Base.metadata.create_all(engine)
        _ctx.push()
        session = Session(bind=engine)
        app.config['TESTING'] = True
        setattr(g, 'sess', session)

        def finish():
            session.close()
            Base.metadata.drop_all(engine)
            engine.dispose()

        request.addfinalizer(finish)
        return session


@fixture
def get_tmp_engine(request):
    _, filename = tempfile.mkstemp()
    engine = create_engine('sqlite:///' + filename)
    request.addfinalizer(functools.partial(os.remove, filename))
    return engine
