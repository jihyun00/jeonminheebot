from jeonminheebot.url import Url


def test_create_url(f_session):
    title = '태양의 탑'
    href = 'http://naver.com'
    url_data = {'href': href, 'title': title}
    find_url = f_session.query(Url) \
                        .filter(Url.href == href) \
                        .first()
    assert not find_url
    url = Url()
    url.create(url_data)
    assert url.href
    assert url.title
    find_existed_url = f_session.query(Url) \
                                .filter(Url.href == href) \
                                .first()
    assert find_existed_url
    assert hasattr(find_existed_url, 'title')
    assert hasattr(find_existed_url, 'href')
    assert find_existed_url.title == title
    assert find_existed_url.href == href
