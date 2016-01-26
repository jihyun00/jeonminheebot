from jeonminheebot.url import Url


def test_create_url(f_session):
    link = 'http://naver.com'
    url = Url(link=link)
    f_session.add(url)
    f_session.commit()
    find_url = f_session.query(Url) \
                        .filter(Url.link == link) \
                        .first()
    assert find_url
    assert hasattr(find_url, 'link')
    assert find_url.link
    assert link == find_url.link
