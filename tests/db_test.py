from jeonminheebot.db import (downgrade_database, get_alembic_config, 
                              get_database_revision, get_session, 
                              initialize_database, upgrade_database)


def test_get_alembic_config(get_tmp_engine):
    assert get_alembic_config(get_tmp_engine)


def test_get_session():
    assert get_session()

