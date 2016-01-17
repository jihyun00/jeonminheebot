from pytest import mark, config

from jeonminheebot.db import open_db, exist_data, insert_data, close_db


real = mark.skipif(not config.getoption('--real'), reason='--real')


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
