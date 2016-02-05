from pytest import mark

from jeonminheebot.url import Url


@mark.parametrize('data', [
    ({'classname': 'test', 'href': 'http://naver.com', 'title': 'reva'}),
    ({'classname': 'aaa', 'href': 'http://google.com', 'title': 'ggg'}),
])
def test_insert_data(f_session, data):
    find_existing_data = f_session.query(Url) \
                                  .filter(Url.classname == data['classname']) \
                                  .one()
    assert not find_existing_data
    find_data = f_session.query(Url) \
                         .filter(Url.classname == data['classname']) \
                         .one()
    assert find_data
