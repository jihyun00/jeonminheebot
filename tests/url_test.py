from jeonminheebot.url import Url


def test_create_url(f_session):
    classname = 'tower'
    href = 'http://naver.com'
    title = '태양의 탑'
    url_data = {'classname': classname, 'href': href, 'title': title}
    find_url = f_session.query(Url) \
                        .filter(Url.href == href) \
                        .first()
    assert not find_url
    url = Url()
    url.create(url_data)
    assert url.href
    assert url.classname
    assert url.title
    find_existed_url = f_session.query(Url) \
                                .filter(Url.href == href) \
                                .first()
    assert find_existed_url
    assert hasattr(find_existed_url, 'classname')
    assert hasattr(find_existed_url, 'href')
    assert hasattr(find_existed_url, 'title')
    assert find_existed_url.classname == classname
    assert find_existed_url.href == href
    assert find_existed_url.title == title
