from pytest import mark, config

from jeonminheebot.db import exist_data, insert_data, close_db


real = mark.skipif(not config.getoption('--real'), reason='--real')


def test_get_engine():
    assert True


@mark.parametrize('engine', [
    (),
])
@real
def test_get_alembic_config(engine):
    assert True


def test_get_session():
    assert True


@mark.parametrize('data', [
    ('http://naver.com/aaa'),
])
@real
def test_exist_data(data):
    assert exist_data(data)


def test_insert_data():
    assert insert_data()


def test_close_db():
    assert close_db()
