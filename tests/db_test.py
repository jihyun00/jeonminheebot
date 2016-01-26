import functools
import os
import tempfile

from pytest import fixture
from sqlalchemy import create_engine
from jeonminheebot.db import (get_alembic_config, initialize_database,
                              get_database_revision, upgrade_database,
                              downgrade_database, get_session, close_db)


@fixture
def get_tmp_engine(request):
    _, filename = tempfile.mkstemp()
    engine = create_engine('sqlite:///' + filename)
    request.addfinalizer(functools.partial(os.remove, filename))
    return engine


def test_get_alembic_config(get_tmp_engine):
    assert get_alembic_config(get_tmp_engine)


def test_initialize_database(get_tmp_engine):
    initialize_database(get_tmp_engine)
    revision = get_database_revision(get_tmp_engine)
    assert revision.is_head


def test_upgrade_database(get_tmp_engine):
    assert upgrade_database(get_tmp_engine)


def test_downgrade_database(get_tmp_engine, revision=''):
    assert downgrade_database(get_tmp_engine, revision)


def test_get_session():
    assert get_session()


def test_close_db():
    assert close_db()
