from pytest import mark, config, raises

from jeonminheebot.db import open_db, exist_data, insert_data, close_db


def test_open_db():
    assert open_db()


def test_exist_data(html):
    assert exist_data(html)


def test_insert_data():
    assert insert_data()


def test_close_db():
    assert close_db()
