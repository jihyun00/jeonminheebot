from jeonminheebot.db import (get_alembic_config, get_session)


def test_get_alembic_config(get_tmp_engine):
    assert get_alembic_config(get_tmp_engine)


def test_get_session():
    assert get_session()

